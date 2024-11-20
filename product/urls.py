from django.urls import path
from .import views

urlpatterns = [
    
    path('product/', views.Get_all_product,name='product'),

    path('product/<str:pk>/',views.get_by_id_product,name='get_by_id_product')


      
]