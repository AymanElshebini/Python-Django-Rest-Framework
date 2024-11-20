from rest_framework import serializers
from .models import Category
class Categoryserializer(serializers.ModelSerializer):
   
  

    class Meta: 
        model=Category
        fields=['id','name','image']