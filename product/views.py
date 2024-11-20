from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse 
from .models import Product
from .serializers import Productserializer
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser 


class productList(generics.ListAPIView):
    serializer_calss=Productserializer
    queryset=Product.objects.all()
    


#Get All Products 
@api_view(['GET'])
def Get_all_product(request):
    products=Product.objects.all()
    serializer=Productserializer(products,many=True)
   # return Response({"product":serializer.data})
    return Response(serializer.data)

#Get One Product
@api_view(['GET'])
def get_by_id_product(request,pk):
    product=get_object_or_404(Product,id=pk)
    serializer=Productserializer(product,many=False)
    return Response({"product":serializer.data})
  


   





