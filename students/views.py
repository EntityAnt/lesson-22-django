from django.core.cache import cache

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from students.models import Student, MyModel
from students.forms import StudentForm
from students.services import StudentService
from users.forms import CustomUserCreationForm


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_detail.html'
    success_url = reverse_lazy('students:student_list')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('students:student_list')


class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'
    context_object_name = 'student_detail'
    success_url = reverse_lazy('students:student_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student_id = self.object.id
        context['full_name'] = StudentService.get_full_name(student_id)
        context['average_grade'] = StudentService.calculate_average_grade(student_id)
        context['has_passed'] = StudentService.has_passed(student_id)
        context['year'] = self.object.year
        return context


class PromoteStudentView(LoginRequiredMixin, View):
    def post(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)

        if not request.user.has_perm('students.can_promote_student'):
            return HttpResponseForbidden("У вас нет прав для перевода студента.")

        # Логика перевода студента на следующий курс
        # student.year = next_year(student.year)
        student.save()

        return redirect('students:student_list')


class ExpelStudentView(LoginRequiredMixin, View):
    def post(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)

        if not request.user.has_perm('students.can_expel_student'):
            return HttpResponseForbidden("У вас нет прав для исключения студента.")

        # Логика исключения студента
        student.delete()

        return redirect('students:student_list')


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        if not self.request.user.has_perm('students.view_student'):
            return Student.objects.none()
        return Student.objects.all()


class MyModelCreateView(CreateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'students/mymodel_form.html'
    success_url = reverse_lazy('students:mymodel_list')


class MyModelListView(ListView):
    model = MyModel
    template_name = 'students/mymodel_list.html'
    context_object_name = 'mymodels'


class MyModelDetailView(DetailView):
    model = MyModel
    template_name = 'students/mymodel_detail.html'
    context_object_name = 'mymodel'


class MyModelUpdateView(UpdateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'students/mymodel_form.html'
    success_url = reverse_lazy('students:mymodel_list')


class MyModelDeleteView(DeleteView):
    model = MyModel
    template_name = 'students/mymodel_confirm_delete.html'
    success_url = reverse_lazy('students:mymodel_list')


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
