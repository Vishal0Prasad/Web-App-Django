# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.contrib import admin

# Register your models here.
admin.site.register(MessLeave)
admin.site.register(MessRefund)
admin.site.register(MessItems)
admin.site.register(OrderHistoryMess)
admin.site.register(OrderListMess)
admin.site.register(MessFeedback)
