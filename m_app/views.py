from rest_framework import viewsets, permissions, status
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view, permission_classes

from django.http import HttpResponse

from .models import User, Event
from django.utils import timezone
from cmap import settings
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer,  EventSerializer

from django.http import JsonResponse
from django.middleware.csrf import get_token

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
   
    def perform_create(self, serializer):
        
        user = User.objects.create_user(email=serializer.validated_data.get('email'), 
                                        phone_number=serializer.validated_data.get('phone_number'),
                                        address=serializer.validated_data.get('address'),
                                        business_name=serializer.validated_data.get('business_name'),
                                        subscription=serializer.validated_data.get('subscription'),
                                        password = serializer.validated_data.get('password')
                                        
                                       
                                        )
        

@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def user_login(request):
    try:
    # if request.method == 'POST':
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        refresh = RefreshToken.for_user(user)
        return Response({"message":"user logged-in",
                            "access_token":str(refresh.access_token),
                            "refresh_token":str(refresh),
                            "user_data": {
                                "user_id": user.id,
                                "email": user.email,
                                "phone":user.phone_number,
                                "address":user.address,
                                "business_name": user.business_name,
                                "subscription": user.subscription,
                                }
                            })
    except ValidationError as e:
        error_details = e.detail
        return Response({"error": "Validation error", "details": error_details}, status=400)

        

    except Exception as e:
        return HttpResponse('This account cannot be logged in due to validation issues')



class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = [IsAuthenticated] 
    permission_classes = [AllowAny]

    # def perform_create(self, serializer):
    #     # Get the logged-in user
    #     user = self.request.user
    #     # Add the logged-in user to the serializer data
    #     serializer.save(user=user)


    def get_queryset(self):
        eventType_param = self.request.query_params.get('EventType', None)

        current_time = timezone.now()
        local_time = timezone.localtime(current_time)
        queryset = Event.objects.filter(date__gte=local_time)
        if eventType_param:
            queryset = queryset.filter(EventType=eventType_param)
        # if queryset:
        #     print('pass')
        return queryset

# def get_queryset(self):
#         event_type_param = self.request.query_params.get('event_type', None)
#         current_time = timezone.now()
#         local_time = timezone.localtime(current_time)
#         queryset = Event.objects.filter(event_datetime__gte=local_time)
#         if event_type_param:
#             queryset = queryset.filter(event_type=event_type_param)
#         # else:
#         #      queryset = Event.objects.all()
#         return queryset