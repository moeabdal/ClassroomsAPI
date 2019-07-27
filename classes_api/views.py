from django.shortcuts import render
from .serializers import *
from classes.models import Classroom
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsOwner


class ClassroomListAPI(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomListSerializer

class ClassroomDetailAPI(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomUpdateSerializer
	lookup_id = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassroomCreateAPI(CreateAPIView):
	serializer_class = ClassroomDetailSerializer
	permission_classes = [IsAuthenticated]
	def perform_create(self, serializer):

		serializer.save(teacher = self.request.user)
	

class ClassroomUpdateAPI(RetrieveAPIView):
	serializer_class = ClassroomUpdateSerializer
	lookup_id = 'id'
	lookup_url_kwarg = 'class_id'
	permission_classes = [IsOwner, IsAuthenticated]


class ClassroomDeleteAPI(DestroyAPIView):
	lookup_id = 'id'
	lookup_url_kwarg = 'classroom_id'
	permission_classes = [IsOwner, IsAuthenticated]

class RegisterAPI(CreateAPIView):
	serializer_class = RegisterSerializer
	
	
