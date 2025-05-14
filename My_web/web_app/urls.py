from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout' ),
    path('todo', views.todo, name='todo'),
    path('update_task/<str:pk>/', views.update_task, name = 'update_task'),
    path('delete_task/<str:pk>/', views.delete_task, name="delete_task"),
    
]
