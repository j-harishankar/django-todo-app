from django.urls import path
from . import views
urlpatterns =[
path('list/', views.task_list, name='list'),
path('', views.create_task, name='create'),
path('complete/<int:task_id>',views.complete,name='complete')
]