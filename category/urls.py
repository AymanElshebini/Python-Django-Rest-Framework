from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.Get_all_Category,name='category'),
    path('category/<str:pk>/',views.get_by_id_category,name='get_by_id_Category')
]







