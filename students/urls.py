from django.urls import path
from . import views
from .views import MyModelCreateView, MyModelListView, MyModelDetailView, MyModelUpdateView, MyModelDeleteView

app_name = 'students'



urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('example/', views.example_view, name='example'),
    path('index/', views.index, name='index'),
    path('student_detail/<int:student_id>', views.student_detail, name='student_detail'),
    path('student/', views.student_list, name='student_list'),
    path('student/new/', views.StudentCreateView.as_view(), name='student_create'),
    path('student/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_update'),


    path('mymodel/', MyModelListView.as_view(), name='mymodel_list'),
    path('mymodel/<int:pk>/', MyModelDetailView.as_view(), name='mymodel_detail'),
    path('mymodel/new/', MyModelCreateView.as_view(), name='mymodel_create'),
    path('mymodel/edit/<int:pk>/', MyModelUpdateView.as_view(), name='mymodel_edit'),
    path('mymodel/delete/<int:pk>/', MyModelDeleteView.as_view(), name='mymodel_delete'),
]