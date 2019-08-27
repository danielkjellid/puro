from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import generic
from django.views.generic.detail import DetailView

from .models import Notes, Supplier
from users.models import User
from .forms import AddNoteForm, UserEditForm

class users(generic.ListView):
    model = User
    template_name = 'backend/users/users.html'

def userDetail(request, pk):
    user = User.objects.get(pk=pk)
    notes = Notes.objects.filter(user_id=pk).order_by('-is_sticky', '-date_edited')
    note_pin = Notes.objects.filter(id = request.GET.get('pin-note-btn'))
    note_delete = Notes.objects.filter(id = request.GET.get('delete-note-btn'))
    
    if request.method == 'POST':
        note_form = AddNoteForm(request.POST)

        if note_form.is_valid():
            note_form.instance.date_edited = timezone.now()
            note_form.instance.user = user
            note_form.instance.author = request.user
            note_form.save()
            messages.success(request, 'Note was successfully created')
            return redirect ('user-detail', pk)

    else:
        note_form = AddNoteForm(request.POST)
    
    #conditional check for deleting notes.
    if request.GET.get('delete-note-btn'):
        note_delete.delete()
        messages.success(request, 'Note was successfully deleted')
        return redirect ('user-detail', pk)

    #conditional check checking if the instance of note clicked is sticky or not
    if request.GET.get('pin-note-btn'):
        if note_pin.filter(is_sticky = True):
            note_pin.update(is_sticky = False)
            messages.success(request, 'Note was successfully unpinned')
        else:
            note_pin.update(is_sticky = True)
            messages.success(request, 'Note was sucessfully pinned')
        return redirect ('user-detail', pk)

    context = {
        'user': user,
        'notes': notes,
        'note_form': note_form,
    }

    return render (request, 'backend/users/users_user.html', context)

def userDetailEdit(request, pk):
    user = User.objects.get(pk=pk)
    notes = Notes.objects.filter(user_id=pk).order_by('-is_sticky', '-date_edited')
    note_pin = Notes.objects.filter(id = request.GET.get('pin-note-btn'))
    note_delete = Notes.objects.filter(id = request.GET.get('delete-note-btn'))
    edit_form = UserEditForm(instance=user)
    note_form = AddNoteForm()
    
    if request.method == 'POST' and 'edit-user-btn' in request.POST:
        edit_form = UserEditForm(request.POST, instance=user)

        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'User was successfully updated')
            return redirect ('user-detail', pk)

        else:
            edit_form = UserEditForm(instance=user)

    if request.method == 'POST' and 'make-note-btn' in request.POST:
        note_form = AddNoteForm(request.POST)

        if note_form.is_valid():
            note_form.instance.date_edited = timezone.now()
            note_form.instance.user = user
            note_form.instance.author = request.user
            note_form.save()
            messages.success(request, 'Note was successfully created')
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

    return render (request, 'backend/users/users_user_edit.html', context)

class suppliers(generic.ListView):
    model = Supplier
    template_name = 'backend/suppliers/suppliers.html'