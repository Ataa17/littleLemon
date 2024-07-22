from django.shortcuts import render
from rest_framework import generics ,viewsets
from .models import menu,booking
from .serializers import MenuSerializer , BookingSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    queryset=menu.objects.all()
    serializer_class=MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer
class bookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset=booking.objects.all()
    serializer_class=BookingSerializer