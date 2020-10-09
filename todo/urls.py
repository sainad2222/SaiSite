from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('',views.todoHome,name='home'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('update_task/<str:pk>',views.updateTask,name='update_task'),
    path('delete_task/<str:pk>',views.deleteTask,name='delete_task')
]
