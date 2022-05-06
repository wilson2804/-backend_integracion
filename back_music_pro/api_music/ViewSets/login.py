from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.contrib.sessions.models import Session
from datetime import datetime
from ..Serializers.ser_UserProfile import UserProfileSerializer 
from ..models import UserProfile
from rest_framework.views import APIView




class Login(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        login_serializer = self.serializer_class(data= request.data, context= {'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                
                token,created = Token.objects.get_or_create(user = user)
                user_serializer = UserProfileSerializer(user)
                
                if created:
                    
                    return Response ({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message' : 'Inicio exitoso'

                    }, status= status.HTTP_201_CREATED)
                else:
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()

                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response ({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message' : 'Inicio exitoso'

                    }, status= status.HTTP_201_CREATED)
            else:
                return Response({ 'mensaje' :'este usuario no puede iniciar sesion'}, 
                                    status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({ 'mensaje' :'nombre de usuario o contraseña incorrecta'}, 
                status = status.HTTP_400_BAD_REQUEST)

class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


"""class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = UserProfile.objects.filter(id=request.data.get('user', 0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Sesión cerrada correctamente.'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe este usuario.'}, status=status.HTTP_400_BAD_REQUEST)
"""

    
