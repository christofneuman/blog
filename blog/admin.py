from django import forms
from django.contrib import admin
from redactor.widgets import RedactorEditor

from blog.models import Blog, ContactMe


class BlogAdminForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = []
        widgets = {
            'body': RedactorEditor(),
        }


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    list_display = ('title', 'published', 'created_at')
    prepopulated_fields = {"slug": ("title",)}


class ContactAdmin(admin.ModelAdmin):
    model = ContactMe
    list_display = ('name', 'email', 'message')


admin.site.register(Blog, BlogAdmin)
admin.site.register(ContactMe, ContactAdmin)
