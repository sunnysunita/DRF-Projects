from django.urls import path, include
from .views import TaskCreateList, TaskRetUpdDes

urlpatterns = [
    path('tasks/', TaskCreateList.as_view(), name='TaskCreateList'),
    path('tasks/<int:pk>', TaskRetUpdDes.as_view(), name='TaskRetUpdDes'),
]