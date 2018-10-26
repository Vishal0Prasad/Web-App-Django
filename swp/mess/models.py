from django.db import models
from datetime import datetime

class MessLeave(models.Model):
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

class MessRefund(models.Model):
	student = models.ForeignKey('accounts.Student', models.DO_NOTHING, blank=True, null=True)
	refund_from=models.DateField(blank=True, null=True)
	refund_to=models.DateField(blank=True, null=True)
	account_number = models.CharField(max_length=18, blank = True, null = True)
	account_holder_name = models.CharField(max_length = 20, blank = True, null = True)
	ifsc_code = models.CharField(max_length = 11, blank = True, null = True)
	ref_amount = models.IntegerField(default=0, blank=True, null=True)
	timestamp = models.DateTimeField(blank=True, null=True)
	created_at = models.DateField(blank=True, null=True)
	created_by = models.CharField(max_length=45, blank=True, null=True)
	modified_at = models.DateField(blank=True, null=True)
	modified_by = models.CharField(max_length=45, blank=True, null=True)

	def __str__(self):
		return '%s %s %s %s' % (self.student.user.username, self.refund_from, self.refund_to, self.ref_amount)

class MessItems(models.Model):
	item_name = models.CharField(max_length=45, blank=False, null=False, unique = True)
	cost = models.FloatField(blank=False, null=False)
	quantity = models.IntegerField()
	timestamp = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return "{}".format(self.item_name)

class OrderHistoryMess(models.Model):
	student = models.ForeignKey('accounts.Student', models.DO_NOTHING, blank=True, null=True)
	item = models.ForeignKey(MessItems, models.DO_NOTHING, blank=True, null=True)
	quantity = models.IntegerField(blank=True, null=True)
	timestamp = models.DateTimeField(blank=True, null=True, auto_now_add=True)
	created_at = models.DateField(blank=True, null=True, auto_now_add=True)
	created_by = models.CharField(max_length=45, blank=True, null=True)
	modified_at = models.DateField(blank=True, null=True)
	modified_by = models.CharField(max_length=45, blank=True, null=True)

	def __str__(self):
		return "{} {}".format(self.student.user.username, self.item.item_name)


class OrderListMess(models.Model):
	student = models.ForeignKey('accounts.Student', models.DO_NOTHING, blank=True, null=True)
	item = models.ForeignKey(MessItems, models.DO_NOTHING, blank=True, null=True)
	quantity = models.IntegerField(blank=True, null=True)
	timestamp = models.DateTimeField(blank=True, null=True, auto_now_add  =True)
	created_at = models.DateField(blank=True, null=True)
	created_by = models.CharField(max_length=45, blank=True, null=True)
	modified_at = models.DateField(blank=True, null=True)
	modified_by = models.CharField(max_length=45, blank=True, null=True)

	def __str__(self):
		return "{}".format(self.student.user.username)


class MessFeedback(models.Model):
	student = models.ForeignKey('accounts.Student', models.DO_NOTHING, blank=True, null=True)
	feedback = models.CharField(max_length=256, blank=True, null=True)
	room_no = models.IntegerField(blank=True, null=True)
	comp_img = models.ImageField(upload_to='images/'+str(datetime.now()),blank=True,null=True)
	timestamp = models.DateTimeField(blank=True, null=True, auto_now_add  =True)
	created_at = models.DateField(blank=True, null=True)
	created_by = models.CharField(max_length=45, blank=True, null=True)
	modified_at = models.DateField(blank=True, null=True)
	modified_by = models.CharField(max_length=45, blank=True, null=True)

	def __str__(self):
		return "{} {}".format(self.student.user.username, self.feedback)
