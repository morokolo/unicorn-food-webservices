from django.shortcuts import render

from .serializers import *
from rest_framework import views, viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
# ViewSets define the view behavior.

@api_view(['POST'])
@permission_classes((AllowAny,))
def create_user(request):
    serialized = UserSerializer(data=request.data['user'])
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
# def create_users(request):
#     data = self.request.data
#     user = User()
#
#     user.username = data['username']
#     user.email = data['email']
#     user.first_name = data['first_name']
#     user.last_name = data['last_name']
#     user.save()
#
#     user.set_password(data['password'])
#     user.save()
#     user_profile = UserProfile()
#     user_profile.user = user
#     user_profile.user_type = 'buyer'
#     user_profile.cellphone = data['cellphone']
#     image = data['image']
#
#     user_profile.save()
#
#     return Response(json.dumps(user_profile))

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    parser_classes = (MultiPartParser, FormParser,)

    #def perform_create(self, serializer):



class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class WaiterViewSet(viewsets.ModelViewSet):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer
