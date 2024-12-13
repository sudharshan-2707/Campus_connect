

from django.db import models
import datetime
import os

class Register(models.Model):
    user_name = models.CharField(max_length=50,null=True)
    first_name = models.CharField(max_length = 20,null=True)
    email = models.EmailField(max_length = 30)
    phone = models.CharField(max_length=50)
    

    def __str__(self):
        return self.user_name

def getFileName(request,filename):
    now_time =datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class Event(models.Model):
    evid=models.IntegerField(null=True)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    description=models.TextField(max_length=150,null=False,blank=False)
    location=models.CharField(max_length=150,null=False,blank=False)
    date=models.DateField(blank=True, null=True)
    time=models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
# Create your models here.
