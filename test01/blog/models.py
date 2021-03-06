from django.db import models
from django.contrib.auth.models import User
from bsddb.test.test_all import verbose

# Create your models here.
class scores(models.Model):
    name = models.CharField(max_length=30)
    score = models.IntegerField()
    lesson_name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['score']

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
    email = models.EmailField()
    
    def __str__(self):
        return u'%s %s %s' % (self.first_name, self.last_name, self.email)
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    
    def __str__(self):
        return self.title
    
class product(models.Model):
    name = models.CharField(max_length=60)
    
