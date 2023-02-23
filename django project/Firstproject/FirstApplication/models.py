from django.db import models

class Name(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class ID(models.Model):
    id_number = models.IntegerField()

class Contact(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

class Address(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
