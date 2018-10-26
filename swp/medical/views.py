from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse
from .forms import MedicalLeaveForm,AppointmentForm
from .models import *
from django.contrib.auth.decorators import login_required
from accounts.models import Student
from dashboard.models import MedicalAnnouncements
import datetime
from django.middleware.csrf import get_token
# Create your views here.
@login_required
def medical_dashboard(request):
    announcements=MedicalAnnouncements.objects.all()
    scrollL_announce=len(announcements)
    if scrollL_announce <= 3:
        scrollL_announce = '140px'
    else:
        scrollL_announce = str(3 * 70)+ 'px'
    return render(request,'medical/medical_dashboard.html',{"announcements":announcements,"doctors":[],'scrollL_announce':scrollL_announce})
@login_required
def medical_message(request):
    return render(request,'medical/medical_message.html')
@login_required
def medical_leave(request):
    form=MedicalLeaveForm()
    return render(request,'medical/medical_leave.html',{'form':form})
@login_required
def sendMessage(request):
    error_message=""
    if request.method == 'POST':
        subject=request.POST['subject']
        to_email='iiitsmedical@gmail.com'   #hardcoded to avoid any hacks
        body=request.POST['body']
        if(len(subject)==0):
            error_message="Subject can't be empty"
            if(len(body)==0):
                error_message="Subject and Message can't be empty"
            return render(request,'medical/medical_message.html',{"error_message":error_message})
        elif(len(body)==0):
            error_message="Message can't be empty"
            return render(request,'medical/medical_message.html',{"error_message":error_message})
        message=render_to_string('medical/message.html',{'from':request.user.username,'body':body})
        email=EmailMessage(subject,message,to=[to_email])
        email.send()
        return render(request,'medical/success.html')
    return render(request,'medical/medical_message.html',{"error_message":error_message})
def getDate(s):
    s=s.split('-')
    year=int(s[0])
    month=int(s[1])
    day=int(s[2])
    return datetime.date(year,month,day)
@login_required
def applyLeave(request):
    if request.method == 'POST':
        form = MedicalLeaveForm(request.POST)
        if form.is_valid():
            leave_form=form.save(commit=False)
            leave_form.student=Student.objects.get(user=request.user)
            leave_form.leave_from=getDate(request.POST['leave_from'])
            leave_form.leave_to=getDate(request.POST['leave_to'])
            leave_form.timestamp=datetime.datetime.now()
            leave_form.created_at=datetime.datetime.now().date()
            leave_form.created_by=request.user.username
            if(leave_form.leave_from>=leave_form.leave_to):
                error_message="Please enter valid From and To dates"
                return render(request, 'medical/medical_leave.html', {
                'form': form,
                'error_message':error_message
                })
            leave_form.save()
            return render(request, 'medical/success.html')
        else:
            error_message="Please enter date in YYYY-MM-DD format"
            return render(request, 'medical/medical_leave.html', {
            'form': form,
            'error_message':error_message
            })
    form = MedicalLeaveForm()
    return render(request, 'medical/medical_leave.html', {
    'form': form,
    'error_message':''
    })
def getDateTime(d,t):
    d=d.split('-')
    t=t.split(':')
    return datetime.datetime(int(d[0]),int(d[1]),int(d[2]),int(t[0]),int(t[1]),0)
@login_required
def searchDoctors(request):
    if request.method=='POST':
        datepicker=request.POST['date']
        timepicker=request.POST['time']
        specialisation=request.POST['specialisation']
        csrf_token=get_token(request)
        mydatetime=getDateTime(datepicker,timepicker)
        docs=[]
        doctors=Doctors.objects.filter(specialisation=specialisation,date=getDate(datepicker))
        #doctors=Doctors.objects.all()
        for doc in doctors:
            if(mydatetime>=getDateTime(str(doc.date),str(doc.available_from)) and mydatetime<=getDateTime(str(doc.date),str(doc.available_till))):
                docs.append(doc)
        return HttpResponse(render_to_string('medical/searchResults.html',context={'csrf_token':csrf_token,'doctors':docs,'len':len(docs),'date':datepicker,'time':timepicker}))
    return HttpResponse(status=500)
@login_required
def bookAppointment(request):
        if request.method == 'POST':
            doc_id=request.POST['radio']
            date=request.POST['mydate']
            time=request.POST['mytime']
            form = AppointmentForm()
            return render(request,'medical/appointment.html',context={'docid':doc_id,'adate':date,'atime':time,'form':form,'error_message':''})
        return redirect('medical_dashboard')

@login_required
def makeAppointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment_form=form.save(commit=False)
            doc_id=request.POST['docid']
            adate=request.POST['adate']
            atime=request.POST['atime']
            appointment_form.appointment_time=getDateTime(adate,atime)
            appointment_form.student=Student.objects.get(user=request.user)
            appointment_form.doctor=Doctors.objects.get(id=doc_id)
            appointment_form.timestamp=datetime.datetime.now()
            appointment_form.created_at=datetime.datetime.now().date()
            appointment_form.created_by=request.user.username
            appointment_form.save()
            return render(request, 'medical/success.html')
        else:
            doc_id=request.POST['docid']
            adate=request.POST['adate']
            atime=request.POST['atime']
            error_message="Please enter valid values"
            return render(request,'medical/appointment.html',context={'docid':doc_id,'adate':date,'atime':time,'form':form,'error_message':error_message})
    return redirect('medical_dashboard')
