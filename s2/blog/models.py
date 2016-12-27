from django.db import models

# Create your models here.

    
class UserInfo(models.Model):
    UserId = models.IntegerField()
    UserName = models.CharField(max_length = 30)
    email = models.EmailField(blank=True)
    
    def __str__(self):
        return self.UserName
    
class CommondityInfo(models.Model):
    CommodityId = models.IntegerField()
    CommodityName = models.CharField(max_length = 30)
    
    
    def __str__(self):
        return self.CommodityName

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    
    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')
    
    def __str__(self):
        return ("%s,%s") % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class OrderInfo(models.Model):
    UserId = models.IntegerField()
    Amount = models.IntegerField()
    CommodityId = models.IntegerField()
    order_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.CommodityId
    
#create account for zhifubao


    #def __str__(self):
     #   return self.pay
    
class Order(models.Model):
    payment = models.CharField(max_length=100,default="", editable=False)
    address = models.CharField(max_length=100,default="", editable=False)
    product_name = models.CharField(max_length=100,default="", editable=False)
    
    def __str__(self):
        return self.product_name
    
    
class Account(models.Model):
    product_price = models.IntegerField()
    order = models.ForeignKey(Order)
    account_date = models.DateField()
    

    
