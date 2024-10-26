from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import RegisterView
from . import views
from .views import MyModelCreateView, MyModelListView, MyModelDetailView, MyModelUpdateView, MyModelDeleteView, \
    StudentListView, StudentCreateView, StudentUpdateView

app_name = 'students'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('example/', views.example_view, name='example'),
    path('index/', views.index, name='index'),
    path('student_detail/<int:student_id>', views.student_detail, name='student_detail'),
    path('', StudentListView.as_view(), name='student_list'),
    path('student/new/', StudentCreateView.as_view(), name='student_create'),
    path('student/<int:pk>/edit/', StudentUpdateView.as_view(), name='student_update'),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page=''), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    path('mymodel/', MyModelListView.as_view(), name='mymodel_list'),
    path('mymodel/<int:pk>/', MyModelDetailView.as_view(), name='mymodel_detail'),
    path('mymodel/new/', MyModelCreateView.as_view(), name='mymodel_create'),
    path('mymodel/edit/<int:pk>/', MyModelUpdateView.as_view(), name='mymodel_edit'),
    path('mymodel/delete/<int:pk>/', MyModelDeleteView.as_view(), name='mymodel_delete'),
]
