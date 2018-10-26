import os
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import HostelAnnouncements, MessAnnouncements, MedicalAnnouncements, ImportantContacts
from accounts.models import Student
from django.contrib.auth.models import User
from .forms import EditUserNameForm, EditBioAvatarForm
from django.http import JsonResponse
from django.views import View
from .forms import PhotoForm
from accounts.models import Student



@login_required
def dashboard_index(request):
    # hostel_announcements = get_list_or_404(HostelAnnouncements, )
    hostel_announcements = list(HostelAnnouncements.objects.all())
    hostel_announcements.sort(key = lambda a: a.timestamp, reverse = True)

    mess_announcements = list(MessAnnouncements.objects.all())
    mess_announcements.sort(key = lambda a: a.timestamp, reverse = True)

    medical_announcements = list(MedicalAnnouncements.objects.all())
    medical_announcements.sort(key = lambda a: a.timestamp, reverse = True)

    return render(request, 'dashboard/index.html', {
    'hostel_announcements': hostel_announcements,
    'mess_announcements': mess_announcements,
    'medical_announcements': medical_announcements
    })

@login_required
def announcement_detail(request, flag, pk):
    if flag == '1':
        announcement = get_object_or_404(HostelAnnouncements, pk = pk)
        return render(request, 'dashboard/announcement.html', {
        'announcement': announcement
        })
    elif flag == '2':
        announcement = get_object_or_404(MessAnnouncements, pk = pk)
        return render(request, 'dashboard/announcement.html', {
        'announcement': announcement
        })
    elif flag == '3':
        announcement = get_object_or_404(MedicalAnnouncements, pk = pk)
        return render(request, 'dashboard/announcement.html', {
        'announcement': announcement
        })

@login_required
def upload_image(request):
    a  = ""
    if len(request.FILES) > 0:
        if request.FILES['myfile']:
            student = get_object_or_404(Student, user = request.user)
            myfile = request.FILES['myfile']
            student.avatar = 'media/images/'+myfile.name
            a = student.bio
            student.save()
    return redirect('/dashboard/profile')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditUserNameForm(data = request.POST, instance=request.user)
        student = get_object_or_404(Student, user = request.user)
        bio_post = request.POST.get("editor")
        if bio_post != '' and student.bio != bio_post:
            student.bio = request.POST.get("editor")
            student.save()
        if form.is_valid():
            form.save()
        return redirect('/dashboard/profile')
    else:
        student = get_object_or_404(Student, user = request.user)
        form = EditUserNameForm(instance=request.user)
        return render(request, 'dashboard/edit_profile.html', {
            'form': form,
            'student': student,
            'bio': student.bio,
        })

# @login_required
# class BasicUploadView(View):
#     def get(self, request):
#         student = get_object_or_404(Student, user = request.user)
#         return render(self.request, 'photos/basic_upload/index.html', {'avatar': student.avatar})
#
#     def post(self, request):
#         form = PhotoForm(self.request.POST, self.request.FILES)
#         if form.is_valid():
#             photo = form.save()
#             data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
#         else:
#             data = {'is_valid': False}
#         return JsonResponse(data)

@login_required
def contacts(request):
    imp_contacts = list(ImportantContacts.objects.all())
    return render(request, 'dashboard/important_contacts.html', {
        'imp_contacts': imp_contacts
    })
