from rest_framework import serializers
from .models import Product

from category.serializers import Categoryserializer



class Productserializer(serializers.ModelSerializer):

      class Meta:
           model=Product
           #fields="__all__"
           fields = ['id','code','name','price_sell','price_offer','ratings','description','image','category']
           #fields=('id','code','name','price_sell','price_offer','ratings','description','image','category')
           
      category = Categoryserializer()   
        
        
      

     