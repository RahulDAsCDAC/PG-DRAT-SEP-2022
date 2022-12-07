from django.urls import path
from pgdratapp import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('addtask', views.addTask, name='Add Task'),
    path('updatetask/<str:pk>/', views.updateTask, name='Update Task'),
    path('displaytask', views.displayTask, name='Display Task'),
    path('deletetask/<str:pk>/', views.deleteTask, name='Delete Task'),
    path('signin', views.signIn, name='Sign In'),
    path('login', views.logIn, name='Log In'),
    path('logout', views.logOut, name='Log Out'),
]