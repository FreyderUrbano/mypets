from django.db import models
from django.db.models.fields import BooleanField, DateTimeField

# Create your models here.
class user(models.Model):
    id = Integer(primary_key=True)
    first_name = VARCHAR(128)
    last_name = VARCHAR(128)
    id_identification = Integer
    number_id = VARCHAR(15)
    id_city = Integer(15)
    email = VARCHAR(200)
    password = VARCHAR(200)
    status = BooleanField
    created_at = DateTimeField
    updated_at = DateTimeField
    deleted_at = DateTimeField