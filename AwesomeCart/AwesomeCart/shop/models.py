from django.db import models
import datetime

# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    category = models.CharField(max_length=500,default="")
    subcategory = models.CharField(max_length=50,default="")
    price= models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/images',default="") 
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=400)
    pub_date = models.DateField()

    def __str__(self):
        return str(self.product_name)
    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50,default=" ")
    email = models.EmailField(max_length = 70,default=" ")
    phone = models.CharField(max_length = 50,default=" ")
    querry = models.TextField(max_length=700,default=" ")
    date = models.DateField(default=datetime.datetime.now())

    def __str__(self):
        return self.name
