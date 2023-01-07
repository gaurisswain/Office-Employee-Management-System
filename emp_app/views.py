from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Employee, Role, Department

def index(request):
    return render(request, 'index.html')

def view_emp(request):
    emps = Employee.objects.all()
    context = {
        'emp': emps,
    }
    return render(request, 'view.html', context)
    
def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        role = int(request.POST['role'])
        department = int(request.POST['department'])
        new_emp = Employee(first_name = first_name, last_name = last_name, department_id = department, role_id = role)
        new_emp.save()
        return HttpResponse("Employee added successfully")
    elif request.method == "GET":
        return render(request, 'add.html')
    else:
        return HttpResponse('An exception Occured!!')



    return render(request, 'add.html')

def remove_emp(request):
    return render(request, 'remove.html')

def filter_emp(request):
    return render(request, 'filter.html')

def main(request):
    template = loader.get_template('master.html')
    return HttpResponse(template.render())
# Create your views here.
