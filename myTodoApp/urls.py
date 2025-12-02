from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.taskView, name = 'home'),
    # path('add/', views.add, name = 'add'),
    # path("done/", views.completed, name = "done"),
    path('addTask', views.addTask, name="addTask"),
    path('markAsDone/<int:pk>/', views.markAsDone, name = 'markAsDone'),
    path('delete/<int:pk>/', views.delete, name = 'delete'),
    path('undone/<int:pk>/',views.undone, name='undone'),
    path('edit/<int:pk>/', views.edit, name= 'edit'),
]