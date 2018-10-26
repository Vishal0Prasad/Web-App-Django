from django.contrib import admin
from .models import MedicalLeave,Doctors,MedicalAppointment

admin.site.register(MedicalLeave)
admin.site.register(Doctors)
admin.site.register(MedicalAppointment)
