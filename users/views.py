import pdfkit

from django.contrib.contenttypes.models import ContentType

from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic.detail import DetailView

from users.models import User, Note
from users.forms import AddNoteForm, EditNoteForm, DeleteNoteForm, EditUserForm, ToggleUserForm, AddUserForm, DivErrorList

from utils.models import ChangeLog

# Function for checking if the user is staff. 
def is_staff(user):
    return user.is_staff

# Function for outputting error string
def errorMessage(action, edited):
    return ('Det skjedde en feil ved %s av %s. Se detaljer nedenfor.' % (action, edited))

# Function for outputting success string
def successMessage(action, edited):
    return ('%s av %s var vellykket.' % (action, edited))

# View for listing all users
class users(generic.ListView):
    model = User
    template_name = 'users/backend/users.html'
    paginate_by = 10
    queryset = User.objects.all()

# View for exporting a list of users to PDF.
def exportUsers(request):

    # Query all users
    users = User.objects.all()

    # Getting template, and rendering data
    template = get_template('exports/users.html')
    html = template.render({'users': users})
    pdf = pdfkit.from_string(html, False)

    # Method for creating file name
    def create_file_name():
        file_name = 'users %s.pdf' % (timezone.now())
        return file_name.strip()

    # Set filename as the filename created by create_file_name() method
    filename = create_file_name()

    # Dump file contents into a response with the appropriate content type
    response = HttpResponse(pdf, content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'

    return response

# View for the backend user detail page
#@login_required
#@user_passes_test(is_staff, login_url='/login')
def user(request, pk):

    # Query appropriate user based on pk returned in url and sticky notes attached to the user
    user = User.objects.get(pk=pk)
    sticky_notes = Note.objects.filter(user_id = pk, is_sticky = True).order_by('date_edited')

    context = {
        'user': user,
        'sticky_notes': sticky_notes
    }

    # Render request, template and context
    return render(request, 'users/backend/user/user.html', context)

# View for adding a new user
def addUser(request):

    # Get the AddUserForm    
    add_user_form = AddUserForm()

    # Show a warning alert on page-load
    messages.warning(request, 'Man kan ikke tildele brukeren en brukergruppe ved å opprette brukeren gjennom dette skjemaet. Brukeren vil automatisk bli lagt til i "privatkunde", men dette kan byttes i etterkant.')

    if request.method == 'POST':

        # Bind data to the form class, and add the error class DivErrorList which adds styling to eventual errors
        add_user_form = AddUserForm(request.POST, error_class=DivErrorList)

        # Validate form inputs
        if add_user_form.is_valid():

            # If the form is valid, save form, add user to group "Privatkunde" and show successmessage
            user = add_user_form.save()
            customer_group = Group.objects.get(name = 'Privatkunde')
            user.roles.add(customer_group)

            # Give the user successful feedback
            messages.success(request, successMessage('Oppretting', 'bruker'))

            # Redirect to the users overview page
            return redirect('users')

        else:
            # If form inputs is invalid, give user feedback
            messages.error(request, errorMessage('oppretting', 'bruker'))

    context = {
        'add_user_form': add_user_form,
    }

    # Render request, template and context
    return render(request, 'users/backend/user/user_add.html', context)

# View for deactivating/activating user
def toggleUser(request, pk):

    # Query appropriate user based on pk returned in url
    user = User.objects.get(pk = pk)

    # Check if the user exists, if not, return 404
    user_to_toggle = get_object_or_404(User, pk = pk)

    if request.method == 'POST':

        # Bind data to the form class, and add the user as instance
        toggle_user_form = ToggleUserForm(request.POST, error_class=DivErrorList, instance = user_to_toggle)

        # Validate form inputs
        if toggle_user_form.is_valid():

            # Check if user is active, and change active state based on result. Redirect to the user profile page.
            if user.is_active == True:
                user.is_active = False
                user.save()

                # Give the user successful feedback
                messages.success(request, 'Brukeren ble deaktivert.')
                return redirect('user', pk)
            
            else:
                user.is_active = True
                user.save()

                # Give the user successful feedback
                messages.success(request, 'Brukeren ble aktivert.')
                return redirect('user', pk)

        else:
            # If form inputs is invalid, give user feedback
            messages.error(request, 'Det skjedde en feil ved deaktivering av bruker. Se detaljer nedenfor.')

    context = {
        'user': user,
    }

    # Render request, template and context
    return render(request, 'users/backend/user/user_edit_toggle.html', context)

# View for editing an existing user
def editUser(request, pk):

    # Query appropriate user based on pk returned in url
    user = User.objects.get(pk = pk)

    # Get the EditUserForm and add the user as instance
    edit_user_form = EditUserForm(instance = user)

    if request.method == 'POST':

        # Bind data to the form class, and add the user as instance
        edit_user_form = EditUserForm(request.POST, error_class=DivErrorList, instance = user)
               
        old_user_instance = User.objects.get(pk = pk)

        # Validate form inputs
        if edit_user_form.is_valid():

            # Save edits
            edit_user_form.save()

            
            # Log change
            ChangeLog.change_message(request.user, User, old_user_instance)
                

            # Give the user successful feedback and redirect
            messages.success(request, successMessage('Redigering', 'bruker'))
            return redirect('user', pk)
        
        else:
            # If form inputs is invalid, give user feedback
            messages.error(request, 'Det skjedde en feil ved redigering av bruker. Se detaljer nedenfor.')
    
    context = {
        'user': user,
        'edit_user_form': edit_user_form,
    }

    # Render request, template and context
    return render(request, 'users/backend/user/user_edit.html', context)

# View for exporting a user profile to PDF
def exportUser(request, pk):

    # Query appropriate user based on pk returned in url and the users group
    user = User.objects.get(pk = pk)
    group = Group.objects.get(user = pk)

    # Getting template, and rendering data
    template = get_template('exports/user.html')
    html = template.render({'user':user, 'group': group})
    pdf = pdfkit.from_string(html, False)

    # Method for creating file name
    def create_file_name(self):
        file_name = '%s-%s-%s.pdf' % (self.first_name, self.last_name, timezone.now())
        return file_name.strip()

    # Set filename as the filename created by create_file_name() method
    filename = create_file_name(user)

    # Dump file contents into a response with the appropriate content type
    response = HttpResponse(pdf, content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'

    return response

# View for listing all notes attached to user
#@login_required
def userNotes(request, pk):

    # Query appropriate user based on pk returned in url
    user = User.objects.get(pk=pk)

    # Query appropriate notes and sticky notes based on pk returned in url and order by date edited.
    notes = Note.objects.filter(user_id=pk, is_sticky=False).order_by('date_edited')
    sticky_notes = Note.objects.filter(user_id=pk, is_sticky=True).order_by('date_edited')

    context = {
        'user': user,
        'notes': notes,
        'sticky_notes': sticky_notes
    }

    # Render request, template and context
    return render(request, 'users/backend/user/user_notes.html', context)

# View for editing an existing note
def editNote(request, pk):

    # Query appropriate note based on pk returned in url
    note = Note.objects.get(pk = pk)

    # Get the EditNoteForm and add the note as instance
    edit_note_form = EditNoteForm(instance = note)

    if request.method == 'POST':

        # Bind data to the form class, and add the note as instance
        edit_note_form = EditNoteForm(request.POST, error_class=DivErrorList, instance = note)

        # Validate form inputs
        if edit_note_form.is_valid():

            # In addition to fields edited, set date_edited to now, and author to request.user
            edit_note_form.instance.date_edited = timezone.now()
            edit_note_form.instance.author = request.user

            # Save edited inputs and instances
            edit_note_form.save()

            # Give the user successful feedback and redirect
            messages.success(request, successMessage('Redigering', 'notat'))
            return redirect ('user', note.user_id)

        else:
            # If form inputs is invalid, give user feedback
            messages.error(request, errorMessage('redigering', 'notat'))

    context = {
        'note': note,
        'edit_note_form': edit_note_form,
    }

    # Render request, template and context
    return render(request, 'users/backend/user/user_notes_edit.html', context)

# View for adding a new note
def addNote(request, pk):

    # Query appropriate user based on pk returned in url and get AddNoteForm()
    user = User.objects.get(pk = pk)
    add_note_form = AddNoteForm()

    if request.method == 'POST':

        # Bind data to the form class
        add_note_form = AddNoteForm(request.POST, error_class=DivErrorList)

        # Validate form inputs
        if add_note_form.is_valid():

            # In adition to the field inputs, add date_edited to now, user queried to user and request.user to author
            add_note_form.instance.date_edited = timezone.now()
            add_note_form.instance.user = user
            add_note_form.instance.author = request.user

            # Save inputs and instances
            add_note_form.save()

            # Give the user successful feedback and redirect
            messages.success(request, 'Oppretting av notat var vellykket')
            return redirect ('user', pk)

        else:
            # If form inputs is invalid, give user feedback
            messages.error(request, 'Det skjedde en feil ved oppretting av notat. Se detaljer nedenfor.')

    context = {
        'user': user,
        'add_note_form': add_note_form,
    }

    # Render request, template and context
    return render(request, 'users/backend/user/user_notes_add.html', context)

# View for deleting note
def deleteNote(request, pk):

    # Query appropriate note based on pk returned in url and get the user attached to the note
    note = Note.objects.get(pk = pk)
    user = User.objects.get(id = note.user_id)

    # Check if the note exists, if not, return 404
    new_to_delete = get_object_or_404(Note, pk = pk)

    if request.method == 'POST':

        # Bind data to the form class, and add the note to delete as instance
        delete_note_form = DeleteNoteForm(request.POST, error_class=DivErrorList, instance = new_to_delete)
        
        # Validate form inputs
        if delete_note_form.is_valid():

            # Delete note
            new_to_delete.delete()

            # Give the user successful feedback and redirect
            messages.success(request, successMessage('Sletting', 'notat'))
            return redirect ('user', user.id)

        else:
            # If form inputs is invalid, give user feedback
            messages.error(request, errorMessage('sletting', 'notat'))
    
    context = {
        'note': note,
        'user': user, 
    }

    # Render request, template and context
    return render(request, 'users/backend/user/user_notes_delete.html', context)

def userChangelog(request, pk):

    user = User.objects.get(pk = pk)
    changelogs = ChangeLog.objects.filter(user_id = pk)

    context = {
        'user': user,
        'changelogs': changelogs,
    }

    return render(request, 'users/backend/user/user_changelog.html', context)



