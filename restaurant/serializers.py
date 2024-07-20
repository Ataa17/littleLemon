from rest_framework import serializers
from .models import menu,booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=menu
        fields=['id','title','price','inventory']

