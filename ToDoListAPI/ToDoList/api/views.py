from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .models import Task
from .serializers import TaskSerializer



# Create your views here.
class TaskCreateList(GenericAPIView, CreateModelMixin, ListModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class TaskRetUpdDes(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

