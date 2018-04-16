from django.contrib import admin
from . import models

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMembers

admin.site.register(models.Group)
