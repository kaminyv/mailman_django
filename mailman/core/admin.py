# -*- coding: utf-8 -*-
"""This is a representation of the models in the admin panel."""

from __future__ import unicode_literals
from django.contrib import admin
from . import models


class ContactInline(admin.TabularInline):
    """Embedded representation of the coupled contact model."""
    model = models.Contact


@admin.register(models.ContactList)
class ContactListAdmin(admin.ModelAdmin):
    """Presenting the contact list model in the admin panel."""
    list_display = ['name', 'created_at', 'updated_at']
    inlines = [ContactInline]


@admin.register(models.MailTemplate)
class MailTemplateAdmin(admin.ModelAdmin):
    """Presenting the mail template model in the admin panel."""
    list_display = ['name', 'created_at', 'updated_at']


@admin.register(models.Mailing)
class MailingAdmin(admin.ModelAdmin):
    """Presenting the mailing model in the admin panel."""
    list_display = ['id', 'created_at', 'description']
