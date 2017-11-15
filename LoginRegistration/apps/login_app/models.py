# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    @staticmethod
    def validate(postData):
        errors = {}
        first_name = postData['first_name']
        last_name = postData['last_name']
        if len(first_name) < 2 or not first_name.isalpha():
            errors['first_name'] = "First name must be more than 2 characters and letters only"
        if len(last_name) < 2 or not last_name.isalpha():
            errors['last_name'] = "Last name must be more than 2 characters and letters only"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email was not properly formed"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters long"
        if postData['password'] != postData['c_password']:
            errors['c_password'] = "confirmation password did not match"

        return errors
