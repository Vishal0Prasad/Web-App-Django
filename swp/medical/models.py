from django.db import models

# Create your models here.
class MedicalLeave(models.Model):
    leave_from=models.DateField(blank=True, null=True)
    leave_to=models.DateField(blank=True, null=True)
    student = models.ForeignKey('accounts.Student', models.DO_NOTHING, blank=True, null=True)
    hometown=models.CharField(max_length=200)
    reason=models.TextField()
    timestamp = models.DateTimeField(blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return '%s %s %s %s' % (self.student.user.username, self.leave_from, self.leave_to, self.reason)

class Doctors(models.Model):
    doctor_name=models.CharField(max_length=100,blank=True, null=True)
    specialisation=models.CharField(max_length=45,blank=True, null=True)
    date=models.DateField(blank=True, null=True)
    available_from=models.TimeField(blank=True, null=True)
    available_till=models.TimeField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.doctor_name,self.date)

class MedicalAppointment(models.Model):
    doctor=models.ForeignKey('medical.Doctors', models.DO_NOTHING, blank=True, null=True)
    student=models.ForeignKey('accounts.Student', models.DO_NOTHING, blank=True, null=True)
    appointment_time=models.DateTimeField(blank=True, null=True)
    problem=models.TextField()
    age=models.IntegerField(blank=True, null=True)
    status_choice=(
		(1,'Male'),
		(2,'Female'),
		(3,'Other'))
    gender=models.IntegerField(choices=status_choice,default=1,blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.student.user.username,self.appointment_time)
