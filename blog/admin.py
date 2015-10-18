from django import forms
from django.contrib import admin
from redactor.widgets import RedactorEditor

from blog.models import Blog


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

admin.site.register(Blog, BlogAdmin)
