from django.shortcuts import render

from .serializers import *
from rest_framework import views, viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
# ViewSets define the view behavior.

@api_view(['POST'])
@permission_classes((AllowAny,))
def create_user(request):
    serialized = UserSerializer(data=request.data['user'])
    user = User()
    if serialized.is_valid():
        user = User.objects.create(**serialized.validated_data)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

    user_profile_data = {}
    user_profile_data['image'] = request.data['image']
    user_profile_data['cellphone'] = request.data['cellphone']
    user_profile_data['user'] = user.id
    user_profile_data['user_type'] = 'buyer'
    user_profile = UserProfileSerializer(data=user_profile_data);

    if user_profile.is_valid():
        user_profile.save()

        token = Token.objects.create(user=user)
        save_data = {}
        save_data['user_profile'] = user_profile.data
        save_data['token'] = token.key

        return Response(save_data, status=status.HTTP_201_CREATED)

    else:
        user.delete()
        return Response(user_profile._errors, status=status.HTTP_400_BAD_REQUEST)



class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    parser_classes = (MultiPartParser, FormParser,)

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class WaiterViewSet(viewsets.ModelViewSet):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer
