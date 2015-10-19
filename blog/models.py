from django.conf import settings
from django.db import models
from django.core.mail import EmailMultiAlternatives
from django.template import loader
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
    image_preview = models.ImageField(upload_to='blogs')
    body = RedactorField(
        verbose_name=u'Text',
        redactor_options={}
    )
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

    def save(self, *args, **kwargs):
        super(ContactMe, self).save(*args, **kwargs)
        txt = loader.render_to_string('email/email.txt', {
            'name': self.name,
            'email': self.email,
            'message': self.message,
        })

        msg = EmailMultiAlternatives(
            subject='Website inquiry from ' + self.email,
            body=txt,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=["christofneuman@hotmail.com"]
        )

        msg.send()
