from django.db import models
from django.contrib.auth.models import User
import datetime
import os
# Create your models here.
## Images Path
def get_file_path(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename="%s%s" % (nowTime,original_filename)
    return os.path.join('images/categery/',filename)



class Category(models.Model):
    name=models.CharField(max_length=255,blank=True,null=True)
    #image=models.ImageField(upload_to='media/categery/%y/%m/%d',default='media/imaged_default/images_d.png')
    image=models.ImageField(upload_to=get_file_path,default='images/imaged_default/images_d.png',blank=True,null=True)
    user=models.name=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    # class Meta:
    #     verbose_name_plural="Categories"