from django.db import models
from django import forms
from django.core.urlresolvers import reverse
from django.db.models import CharField, EmailField
from redactor.fields import RedactorField

# Create your models here.


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)


class Blog(models.Model):
    title = CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    body = RedactorField(verbose_name=u'Text', redactor_options={'plugins': ['imagemanager']})
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ['-created_at']


class ContactMe(models.Model):
    name = CharField(max_length=100)
    email = EmailField(max_length=254)
    message = CharField(max_length=800)
    botcheck = forms.CharField(max_length=5)
