from django import forms
from django.db.models import fields
from .models import Note, Todo, Process, MetaUser
from django.views.generic.edit import FormView
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"


class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = "__all__"


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )


class UserForm(forms.ModelForm):
    class Meta:
        model = MetaUser
        fields = "__all__"


class NoteForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Note
        fields = ["content", ]
