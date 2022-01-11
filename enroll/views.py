from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from enroll.models import StudentInfo,StudentAcademics
from .forms import StudentRegistration,StudentInfoForm

# Create your views here.
def show(request):
    context = {}
    search = request.GET.get('search')
    if search:
        student = StudentInfo.objects.filter(name = search)
    else:
        student = StudentInfo.objects.all()
    context['stu'] = student
    return render(request, 'list.html' , context)