from django.shortcuts import render, request


# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny
from.serializers import ContactSerializer
from .models import Contact




class ContactSerializer(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('name')
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'put', 'delete']

