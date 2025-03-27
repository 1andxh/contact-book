from django.urls import path, include

from rest_framework.routers import DefaultRouter
from . import views
from .views import ContactViewset

# router = DefaultRouter
# router(r'', ContactViewset, name='person')

urlpatterns = [
    # path('', include(router.urls))
    path('view/', views.ContactViewset.view, name='view'),



]
