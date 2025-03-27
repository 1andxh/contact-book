from rest_framework import serializers

from .models import Contact

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = [
            'id',
            'name',
            'phone_number',
            'email'
        ]

def add_contact(request):
    person = Contact.objects.create(
        name='Yao Ming',
        phone_number='0531445623',
        email='mingy@test.com',
    )
    Contact.save()
    
