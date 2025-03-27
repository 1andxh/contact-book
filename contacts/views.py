from django.shortcuts import render
# from django import 


# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny
from.serializers import ContactSerializer
from .models import Contact
from django.http import JsonResponse, request

# person = Contact.objects.create(
#     name='Yao Ming',
#     phone_number='0531445623',
#     email='mingy@test.com'
    
# )

person = [
        {
        'name':'Yao Ming',
        'phone number':'0531445623',
        'email':'mingy@test.com'
    },
        {'name':'kilu Wa',
         'phone number': '0202002025',
         'email':'waki@test.com'   
    },
]
# Contact.save()
class ContactViewset(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('name')
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'put', 'delete']

    def index(request):
        return JsonResponse({'message': 'My Contact Book'})

    def view(self):
        # if request.method == 'GET':
            all_contacts = self.queryset
            response = ContactSerializer(all_contacts, many=True)#many to serialize each item, queryset becomes a list
            return JsonResponse(response.data)
    
    def create(self,request):
        if request.method == 'POST':
            new_contact = Contact.objects.create()
            # person.append(new_contact)
            Contact.save(new_contact)
            return JsonResponse(data=new_contact, safe=False)#safe influences the outcomes of data

    def delete(self,request):
        if request.method == "DELETE":
            pass

    def edit(self, request, pk):
        if request.method == "PUT":
            pass

            

            
