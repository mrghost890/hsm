from django.db import models

# Create your models here.

class Signup(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    state=models.CharField(max_length=200)
    password=models.CharField(max_length=20)
    number = models.CharField(max_length=13)
    Address = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

class Patient(models.Model):
    fullname=models.CharField(max_length=50)
    patientemail=models.EmailField()
    patientdate=models.DateTimeField()
    department=models.CharField(max_length=20)
    patientnumber = models.CharField(max_length=13)
    patientmessage = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname        
