from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import Categoryserializer


#Get All Category
@api_view(['GET'])
def Get_all_Category(request):
    category=Category.objects.all()
    serializer=Categoryserializer(category,many=True)
    return Response({"category":serializer.data})

#Get One Category
@api_view(['GET'])
def get_by_id_category(request,pk):
    category=get_object_or_404(Category,id=pk)
    serializer=Categoryserializer(category,many=False)
    return Response({"category":serializer.data})



  


