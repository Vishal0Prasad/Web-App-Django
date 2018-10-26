from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.CharField(max_length=100, blank=True, null=True)
    roll = models.CharField(max_length=45, blank=True, null=True)
    is_hostel_admin = models.BooleanField(default=False)
    is_mess_admin = models.BooleanField(default=False)
    is_medical_admin = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="images/", default="images/default.png")
    timestamp = models.DateTimeField(blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return str(self.user.username)
