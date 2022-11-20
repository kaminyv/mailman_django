# -*- coding: utf-8 -*-
"""These are the models for the application core."""

from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class DefaultModelField(models.Model):
    """
    A model that represents the default fields for all models.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=User
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ContactList(DefaultModelField):
    """
    A model that represents a list of contacts.
    """
    name = models.CharField(
        'List name',
        max_length=50,
        help_text='Enter a list name'
    )
    description = models.TextField(
        blank=True,
        max_length=200,
        help_text='Enter a list description'
    )

    def __unicode__(self):
        return self.name


class Contact(models.Model):
    """
    A model representing the contact.
    """
    GENDER = [
        ('m', 'male'),
        ('f', 'female'),
    ]

    contact_list = models.ForeignKey(ContactList, on_delete=models.CASCADE)
    email = models.EmailField()
    full_name = models.CharField(
        'Full name',
        blank=True,
        max_length=110,
        help_text='Enter full name or first name.'
    )
    gender = models.CharField(
        'Gender',
        blank=True,
        max_length=1,
        choices=GENDER,
        help_text='Choose a gender.'
    )
    date_of_birth = models.DateField(
        'Date of birth',
        blank=True,
        help_text='Enter the date of birth.',
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Mailing(DefaultModelField):
    """
    The model represents the tasks of sending mail.
    """
    description = models.TextField(
        blank=True,
        max_length=100,
        help_text='Enter a mailing description'
    )
    contact_list = models.ForeignKey('ContactList')
    mail_template = models.ForeignKey('MailTemplate')
    shipment_datetime = models.DateTimeField(blank=True, default=None)


class MailTemplate(DefaultModelField):
    """
    The model presents a mailing list template.
    """
    name = models.CharField('Name template', max_length=50)
    description = models.TextField(
        blank=True,
        max_length=100,
        help_text='Enter the template description.'
    )
    template = models.TextField()

    def __unicode__(self):
        return self.name
