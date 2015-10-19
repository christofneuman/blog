# coding: utf-8

from django import forms

from blog.models import ContactMe


class ContactMeForm(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = [
            'name',
            'email',
            'message'
        ]
