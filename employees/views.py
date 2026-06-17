from django.shortcuts import render
from .models import Employee


def employee_list(request):
    employees = Employee.objects.all()

    search = request.GET.get('search')
    department = request.GET.get('department')

    if search:
        employees = employees.filter(name__icontains=search)

    if department:
        employees = employees.filter(department=department)

    departments = Employee.objects.values_list(
        'department',
        flat=True
    ).distinct()

    return render(
        request,
        'employees/list.html',
        {
            'employees': employees,
            'departments': departments
        }
    )