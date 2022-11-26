from django.urls import path

from .views import index, create, task_del

urlpatterns = [
    path('', index, name='home'),
    path('new-create/', create, name='create'),
    path('task_del/<int:id>/', task_del, name='task_del')
]
