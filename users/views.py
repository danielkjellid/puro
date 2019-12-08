import pdfkit

from django.contrib import messages
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic.detail import DetailView

from users.models import User, Note
from users.forms import AddNoteForm, UserEditForm

# Updated to fit new style
class users(generic.ListView):
    model = User
    template_name = 'users/b_users.html'
    paginate_by = 10
    queryset = User.objects.all()


# Not updated
def usersExport(request):
    users = User.objects.all()

    # getting template, and rendering data
    template = get_template('old/backend/users/users_export.html')
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

def userDetail(request, pk):
    user = User.objects.get(pk=pk)
    
    context = {
        'user': user,
    }

    return render (request, 'users/b_users_user.html', context)

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

    return render (request, 'old/backend/users/users_user_edit.html', context)

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

    return render(request, 'old/backend/users/users_user_edit_toggle.html', context)

def userDetailExport(request, pk):
    user = User.objects.get(pk = pk)
    user_group = Group.objects.get(user = pk)

    # getting template, and rendering data
    template = get_template('old/backend/users/users_user_detail_export.html')
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


