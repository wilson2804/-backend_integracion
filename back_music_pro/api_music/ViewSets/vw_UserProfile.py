from logging import raiseExceptions
from ..models import UserProfile

from rest_framework import viewsets
from ..Serializers.ser_UserProfile import UserProfileSerializer 
from django.views.decorators.csrf import csrf_exempt


import json 


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    handler500 = "rest_framework.exceptions.server_error"
    handler400 = "rest_framework.exceptions.bad_request"





     



