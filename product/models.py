from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from category.models import Category
import datetime
import os


    ## Images Path
def get_file_path(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename="%s%s" % (nowTime,original_filename)
    return os.path.join('images/product/',filename)

class Product(models.Model):
   # product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_in_batch")
    category=models.ForeignKey(Category,on_delete=models.CASCADE, related_name='category')
    code=models.CharField(max_length=255)
    name=models.CharField(max_length=255,blank=True,null=True)
    price_sell=models.DecimalField(max_digits=7,decimal_places=2,default=0,blank=True,null=True)
    price_offer=models.DecimalField(max_digits=7,decimal_places=2,default=0,blank=True,null=True)
    stock=models.IntegerField(default=0)
    ratings=models.DecimalField(max_digits=3,decimal_places=2,default=0)
    description=models.TextField(max_length=1000,default="",blank=True,null=True)
    is_active = models.BooleanField(default=True)
    image=models.ImageField(upload_to=get_file_path,default='images/imaged_default/images_d.png')
    user=models.name=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class ProductImages(models.Model):
    productid=models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True,related_name='images')
    images=models.ImageField(upload_to=get_file_path,default='images/imaged_default/images_d.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


    # def __str__(self):
    #     return self.Product.name