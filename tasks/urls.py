from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/add', views.add_task, name='add_task'),
    path('tasks/drop/<int:pk>', views.drop_task, name='drop_task'),
    path('tasks/edit/<int:pk>', views.edit_task, name='edit_task'),
]