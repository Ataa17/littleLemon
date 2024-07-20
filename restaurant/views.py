from django.shortcuts import render
from rest_framework import generics ,viewsets
from .models import menu,booking
from .serializers import MenuSerializer , BookingSerializer
# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    queryset=menu.objects.all()
    serializer_class=MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer

class bookingViewSet(viewsets.ModelViewSet):
    queryset=booking.objects.all()
    serializer_class=BookingSerializer