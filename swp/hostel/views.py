from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .models import *
from .forms import *
from dashboard.models import HostelAnnouncements
from django.contrib.auth.decorators import login_required
from accounts.models import Student
import datetime

# Create your views here.

@login_required
def hostel_dashboard(request):
	h_announce = HostelAnnouncements.objects.all()
	scrollL_announce = len(h_announce)
	if scrollL_announce <= 3:
		scrollL_announce = '140px'
	else:
		scrollL_announce = str(3 * 70)+ 'px'

	self_help = SelfHelpGroup.objects.all()
	scrollL_self = len(self_help)

	if scrollL_self <= 3:
		scrollL_self = '70px'
	else:
		scrollL_self = str(3 * 70)+ 'px'

	courier_data = Courrier.objects.all()
	#.filter(student=Student.objects.get(user = request.user))
	courier_data = list(filter(lambda x: x.student.user == request.user, courier_data))
	scrollL_courier = len(courier_data)
	if scrollL_courier <= 3:
		scrollL_courier = '140px'
	else:
		scrollL_courier = str(3 * 70)+ 'px'
	context = {'h_announce':h_announce , 'self_help':self_help , 'courier_data':courier_data,
	'scrollL_announce':scrollL_announce,'scrollL_self':scrollL_self,'scrollL_courier':scrollL_courier}
	return render(request,'hostel/hostel_dashboard.html',context)

@login_required
def leave_form(request):
	form = HostelLeaveForm()
	return render(request,'hostel/leave.html',{'form':form})

@login_required
def complaint_form(request):
	form = HostelComplaintForm()
	return render(request,'hostel/complaint.html',{'form':form})

'''@login_required
def complaint_ack(request):
	return render(request,'hostel/complaint-ack.html')'''

def getDate(dat):
	dat = dat.split('-')
	year = int(dat[0])
	month = int(dat[1])
	day = int(dat[2])

	return datetime.date(year,month,day)

@login_required
def addComplaint(request):
	if request.method == 'POST':
		form = HostelComplaintForm(request.POST,request.FILES)
		if form.is_valid():
			complaint_form = form.save(commit=False)
			complaint_form.student = Student.objects.get(user = request.user)
			subject = request.POST['subject']
			complaint_form.complaint = subject + request.POST['complaint']
			if len(request.FILES) > 0:
				complaint_form.comp_img = request.FILES['image']
			else:
				complaint_form.comp_img = ""
			complaint_form.room_no = request.POST['room_no']
			complaint_form.completed = False
			complaint_form.timestamp = datetime.datetime.now()
			complaint_form.created_at = datetime.datetime.now().date() 
			complaint_form.created_by = Student.objects.get(user = request.user)
			complaint_form.modified_at = datetime.datetime.now().date()
			complaint_form.modified_by = Student.objects.get(user = request.user)
			complaint_form.save()
			return render(request,'hostel/complaint-ack.html')
	else:
		form =  HostelComplaintForm()
		return render(request,'hostel/complaint.html',{'form':form,'error_message':''})


	

@login_required
def applyHostelLeave(request):
	if request.method == 'POST':
		form = HostelLeaveForm(request.POST)
		if form.is_valid():
			leave_form = form.save(commit=False)
			leave_form.student = Student.objects.get(user = request.user)
			leave_form.leave_from = getDate(request.POST['leave_from'])
			leave_form.leave_to = getDate(request.POST['leave_to'])
			leave_form.timestamp = datetime.datetime.now()
			leave_form.created_at = datetime.datetime.now().date()
			leave_form.modified_at = datetime.datetime.now().date()
			
			leave_form.created_by = Student.objects.get(user = request.user)
			leave_form.modified_by = Student.objects.get(user = request.user)

			mess_leave = request.POST['select_opt']
#--------------------------------------------------------------------------------------------
			if(mess_leave=='Yes'):
				#Update the mess models with creating an instance of the mess models
				print(mess_leave)
#--------------------------------------------------------------------------------------------
			if(leave_form.leave_from >=  leave_form.leave_to):
				error_message = "Please enter valid From and TO dates"
				return render(request,'hostel/leave.html',{'form':form,'error_message':error_message})
			leave_form.save()
			return render(request, 'hostel/leave-ack.html')
		else:
			error_message = "Please enter data in YYYY-MM-DD format"
			return render(request,'hostel/leave.html',{'form':form,'error_message':error_message})

	form =  HostelLeaveForm()
	return render(request,'hostel/leave.html',{'form':form,'error_message':''})
