import pdfkit

from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic.detail import DetailView

from users.models import User, Note
from users.forms import AddNoteForm, EditNoteForm, DeleteNoteForm, EditUserForm

# Updated to fit new style
def is_staff(user):
    return user.is_staff


class users(generic.ListView):
    model = User
    template_name = 'users/backend/users.html'
    paginate_by = 10
    queryset = User.objects.all()

#@login_required
#@user_passes_test(is_staff, login_url='/login')
def user(request, pk):
    user = User.objects.get(pk=pk)
    sticky_notes = Note.objects.filter(user_id=pk, is_sticky=True).order_by('date_edited')

    context = {
        'user': user,
        'sticky_notes': sticky_notes
    }

    return render(request, 'users/backend/user/user.html', context)

def editUser(request, pk):
    user = User.objects.get(pk = pk)
    edit_user_form = EditUserForm(instance = user)

    if request.method == 'POST':
        edit_user_form = EditUserForm(request.POST, instance = user)

        if edit_user_form.is_valid():
            edit_user_form.save()
            return redirect('user', pk)
        
        else:
            edit_user_form = EditUserForm(instance = user)
    
    context = {
        'user': user,
        'edit_user_form': edit_user_form,
    }

    return render(request, 'users/backend/user/user_edit.html', context)



#@login_required
def userNotes(request, pk):
    user = User.objects.get(pk=pk)
    notes = Note.objects.filter(user_id=pk, is_sticky=False).order_by('date_edited')
    sticky_notes = Note.objects.filter(user_id=pk, is_sticky=True).order_by('date_edited')

    context = {
        'user': user,
        'notes': notes,
        'sticky_notes': sticky_notes
    }

    return render(request, 'users/backend/user/user_notes.html', context)

def editNote(request, pk):
    note = Note.objects.get(pk = pk)
    edit_note_form = EditNoteForm(instance = note)

    if request.method == 'POST':
        edit_note_form = EditNoteForm(request.POST, instance = note)

        if edit_note_form.is_valid():
            edit_note_form.instance.date_edited = timezone.now()
            edit_note_form.instance.author = request.user
            edit_note_form.save()
            return redirect ('user', note.user_id)

        else:
            edit_note_form = EditNoteForm(instance = note)

    context = {
        'note': note,
        'edit_note_form': edit_note_form,
    }

    return render(request, 'users/backend/user/user_notes_edit.html', context)

def addNote(request, pk):
    user = User.objects.get(pk = pk)
    add_note_form = AddNoteForm()

    if request.method == 'POST':
        add_note_form = AddNoteForm(request.POST)

        if add_note_form.is_valid():
            add_note_form.instance.date_edited = timezone.now()
            add_note_form.instance.user = user
            add_note_form.instance.author = request.user
            add_note_form.save()
            return redirect ('user', pk)

        else:
            add_note_form = AddNoteForm()

    context = {
        'user': user,
        'add_note_form': add_note_form,
    }

    return render(request, 'users/backend/user/user_notes_add.html', context)

def deleteNote(request, pk):
    note = Note.objects.get(pk = pk)
    user = User.objects.get(id = note.user_id)

    new_to_delete = get_object_or_404(Note, pk = pk)

    if request.method == 'POST':
        delete_form = DeleteNoteForm(request.POST, instance = new_to_delete)
        
        if delete_form.is_valid():
            new_to_delete.delete()
            return redirect ('user', user.id)

        else:
            delete_form = DeleteNoteForm(instance = new_to_delete)
    
    context = {
        'note': note,
        'user': user, 
    }

    return render(request, 'users/backend/user/user_notes_delete.html', context)



# Not updated
"""
def usersExport(request):
    users = User.objects.all()

    # getting template, and rendering data
    template = get_template('old/backend/users_export.html')
    html = template.render({'users': users})
    pdf = pdfkit.from_string(html, False)

    #function for creating file name
    def create_file_name():
        file_name = 'users %s.pdf' % (timezone.now())
        return file_name.strip()

    filename = create_file_name()

    response = HttpResponse(pdf, content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
    
    return response

def userDetailEdit(request, pk):
    user = User.objects.get(pk=pk)
    notes = Note.objects.filter(user_id=pk).order_by('-is_sticky', '-date_edited')
    note_pin = Note.objects.filter(id = request.GET.get('pin-note-btn'))
    note_delete = Note.objects.filter(id = request.GET.get('delete-note-btn'))
    edit_form = UserEditForm(instance=user)
    note_form = AddNoteForm()
    
    # form validation upon updating user details
    if request.method == 'POST' and 'edit-user-btn' in request.POST:
        edit_form = UserEditForm(request.POST, instance=user)

        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'User was successfully updated!')
            return redirect ('user-detail', pk)

        else:
            edit_form = UserEditForm(instance = user)

    # form validation upon creating new note
    elif request.method == 'POST' and 'make-note-btn' in request.POST:
        note_form = AddNoteForm(request.POST)

        if note_form.is_valid():
            note_form.instance.date_edited = timezone.now()
            note_form.instance.user = user
            note_form.instance.author = request.user
            note_form.save()
            messages.success(request, 'Note was successfully created!')
            return redirect ('user-detail-edit', pk)

        else:
            note_form = AddNoteForm()

    #conditional check for deleting notes.
    if request.GET.get('delete-note-btn'):
        note_delete.delete()
        return redirect ('user-detail-edit', pk)

    #conditional check checking if the instance of note clicked is sticky or not
    if request.GET.get('pin-note-btn'):
        if note_pin.filter(is_sticky = True):
            note_pin.update(is_sticky = False)
        else:
            note_pin.update(is_sticky = True)
        return redirect ('user-detail-edit', pk)

    context = {
        'user_edit_form': edit_form,
        'note_form': note_form,
        'user': user,
        'notes': notes,
    }

    return render (request, 'old/backend/users_user_edit.html', context)

def userDetailEditToggleActive(request, pk):
    user = User.objects.get(pk = pk)
    notes = Note.objects.filter(user_id=pk).order_by('-is_sticky', '-date_edited')
    note_pin = Note.objects.filter(id = request.GET.get('pin-note-btn'))
    note_delete = Note.objects.filter(id = request.GET.get('delete-note-btn'))
    note_form = AddNoteForm()

    # conditional check for deactivating/reactivating users
    if request.method == 'POST' and 'user-toggle-btn' in request.POST:
        
        if user.is_active == True:
            user.is_active = False
            user.save()
            messages.success(request, 'User was successfully deactivated, and will no longer be able to log in.')
            return redirect ('user-detail', pk)
        else:
            user.is_active = True
            user.save()
            messages.success(request, 'User was successfully reactivated, and will now be able to log in.')
            return redirect ('user-detail', pk)

    context = {
        'user': user,
        'note_form': note_form,
        'notes': notes,
    }

    return render(request, 'old/backend/users_user_edit_toggle.html', context)

def userDetailExport(request, pk):
    user = User.objects.get(pk = pk)
    user_group = Group.objects.get(user = pk)

    # getting template, and rendering data
    template = get_template('old/backend/users_user_detail_export.html')
    html = template.render({'user':user, 'user_group': user_group})
    pdf = pdfkit.from_string(html, False)

    #function for creating file name
    def create_file_name(self):
        file_name = '%s-%s-%s.pdf' % (self.first_name, self.last_name, timezone.now())
        return file_name.strip()

    filename = create_file_name(user)

    response = HttpResponse(pdf, content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'

    return response

"""


