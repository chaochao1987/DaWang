from django.db import models

# Create your models here.
class OrderInfo(models.Model):
    UserId = models.IntegerField()
    Amount = models.IntegerField()
    CommodityId = models.IntegerField()

class UserInfo(models.Model):
    UserId = models.IntegerField()
    UserName = models.CharField(max_length = 30)
    
class CommondityInfo(models.Model):
    CommodityId = models.IntegerField()
    CommodityName = models.CharField(max_length = 30)
    
    