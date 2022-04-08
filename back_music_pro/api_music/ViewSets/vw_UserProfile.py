from logging import raiseExceptions
from ..models import UserProfile
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from ..Serializers.ser_UserProfile import UserProfileSerializer 
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.response import Response
import json 

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    handler500 = "rest_framework.exceptions.server_error"
    handler400 = "rest_framework.exceptions.bad_request"

  
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "isok": True
            }
        )


    """@action(detail=False, methods=['POST'], url_path='login')
    def login(self, request):
        data_json = json.loads(request.body.decode("utf-8"))
        result = False
        try:
            pass_to_evaluate = data_json["ms_psw"]
            resultObject = UserProfile.objects.get(
                email=data_json["ms_user"], password=pass_to_evaluate
            )
            
            
            token, created = Token.objects.get_or_create(user=resultObject)
            
            
            result = True
        except Exception as error:
            result = False
            print (error)
        return JsonResponse({"result": result})"""

    

    