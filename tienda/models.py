from django.db import models
from django.db.models.fields import BooleanField, DateTimeField

# Create your models here.
class user(models.Model):
    id = models.IntegerField.primary_key = True
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=128)
    id_identification_type = models.IntegerField
    id_city = models.IntegerField
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    status = models.BooleanField
    created_at = models.DateTimeField
    updated_at = models.DateTimeField
    deleted_at = models.DateTimeField

class Session(models.Model):
    id = models.IntegerField.primary_key = True
    id_user = models.IntegerField
    ip = models.CharField(max_length = 200)
    status = models.BooleanField
    created_at = models.DateTimeField
    updated_at = models.DateTimeField
    deleted_at = models.DateTimeField

class Identification_type(models.Model):
    id = models.IntegerField(20).primary_key = True
    type = models.CharField(max_length = 150)
    abrow = models.CharField(max_length = 4)
    created_at = models.DateTimeField
    updated_at = models.DateTimeField
    deleted_at = models.DateTimeField

class City(models.Model):
    id = models.IntegerField
    code = models.CharField(max_length = 10)
    name = models.CharField(max_length = 150)
    abrev = models.CharField(max_length = 4)
    id_country = models.IntegerField
    status = models.BooleanField
    created_at = models.DateTimeField
    updated_at = models.DateTimeField
    deleted_at = models.DateTimeField

class Country(models.Model):
    id = models.IntegerField
    code = models.CharField(max_length = 10)
    name = models.CharField(max_length = 150)
    abrev = models.CharField(max_length = 4)
    status = models.BooleanField
    created_at = models.DateTimeField
    updated_at = models.DateTimeField
    deleted_at = models.DateTimeField

class Pet(models.Model):
    id = models.IntegerField
    code = models.CharField(max_length = 10)
    name = models.CharField(max_length = 150)
    status = models.BooleanField
    id_user = models.IntegerField
    id_type = models.IntegerField
    id_race = models.IntegerField
    created_at = models.DateTimeField
    updated_at = models.DateTimeField
    deleted_at = models.DateTimeField

class Type(models.Model):
    id = models.IntegerField
    code = models.CharField(max_length = 100)
    name = models.CharField(max_length = 150)
    abrev = models.CharField(max_length = 4)
    status = models.BooleanField
    created_at = models.DateTimeField
    updated_at = models.DateTimeField
    deleted_at = models.DateTimeField

class Race(models.Model):
    id = models.IntegerField
    code = models.CharField(max_length = 10)
    name = models.CharField(max_length = 150)
    abrev = models.CharField(max_length = 4)
    status = models.BooleanField
    created_at = models.DateTimeField
    updated_at = models.DateTimeField
    deleted_at = models.DateTimeField



