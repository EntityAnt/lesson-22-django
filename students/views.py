from django.shortcuts import render
from django.http import HttpResponse

from students.models import Student


def about(request):
    return render(request, 'students/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f'Спасибо, {name}! Сообщение доставлено!')
    return render(request, 'students/contact.html')


def example_view(request):
    return render(request, 'students/example.html')


def index(request):
    student = Student.objects.get(id=10)
    context = {
        'student_name': f'{student.first_name} {student.last_name}',
        'student_year': student.get_year_display(),
    }
    return render(request, 'students/index.html', context=context)


def student_detail(request, student_id: int):
    student = Student.objects.get(id=student_id)
    context = {
        'student': student,
    }
    return render(request, 'students/student_detail.html', context=context)


def student_list(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students/student_list.html', context)

