from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)
    
    
class Address(models.Model):
    city =models.CharField(max_length = 50)
 
class Student(models.Model):
    name= models.CharField(max_length = 50)
    age = models.SmallIntegerField(default = 7)
    address = models.ForeignKey(Address, verbose_name="Address", on_delete=models.CASCADE)

class Address2(models.Model):
    city =models.CharField(max_length = 50)
    def __str__(self):
        return self.city
 
class Student2(models.Model):
    name= models.CharField(max_length = 50)
    age = models.SmallIntegerField(default = 7)
    address = models.ManyToManyField(Address2)


class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')

