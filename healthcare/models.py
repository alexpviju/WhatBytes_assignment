from django.db import models

from django.db import models
from django.conf import settings

class Patient(models.Model):
    gender_choice=[('male','Male'),('female','Female'),('others','Others')]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patients'
    )
    full_name = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    phn_num=models.CharField(max_length=13)
    gender = models.CharField(choices=gender_choice,null=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    

class Doctor(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctors'
    )
    full_name = models.CharField(max_length=150)
    specialization = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(help_text="Experience in years")
    contact_number = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='mappings')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='mappings')
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.full_name} : {self.doctor.full_name}"