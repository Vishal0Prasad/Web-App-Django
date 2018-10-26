from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .import views

app_name = 'hostel'

#Add urls with approriate for leave message and complaint register

urlpatterns = [
    url(r'^$',views.hostel_dashboard, name = 'hostel_dashboard'),
    url(r'^leave_form$',views.leave_form, name = 'leave_form'),
    url(r'^applyHostelLeave$',views.applyHostelLeave, name = 'applyHostelLeave'),
    #url(r'^complaint_ack$',views.complaint_ack,name='complaint_ack'),
    url(r'^form_complaint$',views.complaint_form,name='form_complaint'),
    #url(r'^sendmessage$',views.sendMessage, name = 'sendmessage'),
    url(r'^addComplaint$',views.addComplaint, name = 'addComplaint'),
]

if settings.DEBUG: 
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
