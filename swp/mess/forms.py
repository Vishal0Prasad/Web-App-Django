from django import forms
from .models import MessRefund
from .models import MessLeave
from .models import MessFeedback

# Create refund forms

class MessLeaveForm(forms.ModelForm):
	leave_from=forms.DateField(label='leave_from',input_formats=['%Y-%m-%d'],widget=forms.DateInput(format = '%Y-%m-%d',attrs={"class":"form-control","id":"from_date","name":"date","placeholder":"YYYY-MM-DD","type":"text"}))
	leave_to=forms.DateField(label='leave_to',input_formats=['%Y-%m-%d'],widget=forms.DateInput(format = '%Y-%m-%d',attrs={"class":"form-control","id":"to_date","name":"date1","placeholder":"YYYY-MM-DD","type":"text"}))
	hometown=forms.CharField(label='hometown',widget=forms.TextInput(attrs={"class":"form-control"}))
	reason=forms.CharField(label='reason',widget=forms.Textarea(attrs={"class":"form-control","rows":"4","cols":"50"}))
	class Meta:
		model = MessLeave
		fields = ['leave_from','leave_to','hometown','reason']

class MessRefundForm(forms.ModelForm):
	refund_from=forms.DateField(label='refund_from',input_formats=['%Y-%m-%d'],widget=forms.DateInput(format = '%Y-%m-%d',attrs={"class":"form-control","id":"from_date","name":"date","placeholder":"YYYY-MM-DD","type":"text"}))
	refund_to=forms.DateField(label='refund_to',input_formats=['%Y-%m-%d'],widget=forms.DateInput(format = '%Y-%m-%d',attrs={"class":"form-control","id":"to_date","name":"date1","placeholder":"YYYY-MM-DD","type":"text"}))
	account_number=forms.CharField(label='account_number',widget=forms.TextInput(attrs={"class":"form-control"}))
	account_holder_name=forms.CharField(label='account_holder_name',widget=forms.TextInput(attrs={"class":"form-control"}))
	ifsc_code = forms.CharField(label='ifsc_code',widget=forms.TextInput(attrs={"class":"form-control"}))
	class Meta:
		model = MessRefund
		fields = ['refund_from','refund_to','account_number','account_holder_name','ifsc_code']

class MessFeedbackForm(forms.ModelForm):
	subject = forms.CharField(label='subject',widget=forms.TextInput(attrs={"type":"text","name":"title","placeholder":"Enter subject","width": "600px"}))
	feedback = forms.CharField(label='feedback',widget=forms.Textarea(attrs = {"name":"complaint","placeholder":"Please Enter your complaint here.","cols": "85","height": "60px", "width": "400px"}))
	room_no = forms.CharField(label='room_no',widget=forms.TextInput(attrs={"type":"text","name":"room_no","placeholder":"Enter your room number","width": "300px"}))

	class Meta:
		model = MessFeedback
		fields = ['subject','feedback','room_no']
