from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    firebase_uid = models.CharField(max_length=128, unique=True, null=True)  # Allow null values temporarily
    email = models.EmailField(max_length=277)
    def __str__(self):
        return self.name



