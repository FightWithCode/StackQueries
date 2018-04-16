from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
User = get_user_model()
from django import template
register = template.Library()

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=25, unique=True)
    slug = models.SlugField(unique=True, allow_unicode=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, blank=True, default='')
    members = models.ManyToManyField(User, through='GroupMembers')

    def __str__(self):
        return self.name
    def save(self, *args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = self.description
        super().save(*args, **kwargs)

    class Meta():
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug':self.slug})


class GroupMembers(models.Model):
    group = models.ForeignKey(Group, related_name='member')
    user = models.ForeignKey(User, related_name='user_groups')

    def __str__(self):
        return self.user.username

    class Meta():
        unique_together = ('group', 'user')
