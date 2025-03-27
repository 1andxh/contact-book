from django.urls import path, i

from rest_framework.routers import DefaultRouter
from . import views
from .views import view, create

# router = DefaultRouter
# router(r'', ContactViewset, name='person')

urlpatterns = [
    # path('', include(router.urls))
    path('view/', view, name='view'),
    path('create/', create, name='create')



]
