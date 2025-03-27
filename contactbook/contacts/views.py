from django.shortcuts import render, request


# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny
from.serializers import ContactSerializer
from .models import Contact
from django.http import JsonResponse

person = Contact.objects.create(
    {'name':'Yao Ming',
    'phone_number':'0531445623',
    'email':'mingy@test.com'}
    
)
Contact.save()
class ContactSerializer(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('name')
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'put', 'delete']

   # person = Contact.objects.create(
    #     name='Yao Ming',
    #     phone_number='0531445623',
    #     email='mingy@test.com',
    # )
    # Contact.save()
    def view_contacts(request):
    
        if request.method == 'GET':
            all_contacts = Contact.objects.all()
            serializer = ContactSerializer(all_contacts, many=True)#many to serialize each item, it becomes a list
            return JsonResponse(serializer.data)