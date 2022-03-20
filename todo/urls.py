from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiOverview),
    path('register/', views.register),
    path('login/', views.login),
    path('todos/', views.get_one_todo),
    path('todos/create/', views.add_todo),
    path('todos/<int:pk>/update/', views.update_todo),
    path('todos/<int:pk>/delete/', views.delete_todo),
]
