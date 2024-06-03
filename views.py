from django.shortcuts import render

from hola.models import *

from django.core.paginator import Paginator

# importing queue for or operation in search
from django.db.models import Q

# Create your views here.
def get_student(request):
    # to apply search on multiple objects

    queryset=Student.objects.all()
    if request.GET.get('search'):
        search=request.GET.get('search')
        # double _ in icontains
        # we will apply or condition in search bar to get distinct data from different columns
        # we use double _ fro department here
        queryset=queryset.filter(
           Q( student_name__icontains=search)|
           Q(student_id__student_id__icontains=search)|
           Q(student_email__icontains=search)|
           Q(department__department__icontains=search)|
           Q(student_age__icontains=search)

           
           )


    # return render(request,'report/student.html',{'queryset':queryset})

    paginator = Paginator(queryset, 25) 
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    return render(request,'report/student.html',{'queryset':page_obj})
