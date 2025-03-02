from django.shortcuts import render
from rest_framework import generics
from .models import Menu, Booking
from django.contrib.auth.models import User
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import permissions

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'index': reverse('index', request=request, format=format),
        'menu-list': reverse('menu-list', request=request, format=format),
        'user-list': reverse('user-list', request=request, format=format),
        'booking-list': reverse('booking-list', request=request, format=format),
        'api-token-auth': reverse('api-token-auth', request=request, format=format),
    })

def index(request):
    return render(request, 'index.html',{})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    