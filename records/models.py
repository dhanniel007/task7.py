from django.db import models

# Create your models here.

class Address (models.Model):
    Name = models.CharField(max_length=10000)
    Country = models.CharField(max_length=10000)
    State=  models.CharField(max_length=10000)
    City =  models.CharField(max_length=10000)
    House_address=  models.CharField(max_length=10000 )

    def __str__(self):
        return self.House_address

class Doctor (models.Model):
    Doctor_name = models.CharField(max_length=10000)
    Hospital_name =  models.CharField(max_length=10000)
    Hospital_address =  models.CharField(max_length=10000)
    
    
    def __str__(self):
        return self.Doctor_name

class Product (models.Model):
    Product_name = models.CharField(max_length=50)
    Product_price =  models.CharField(max_length=10000)

    def __str__(self):
        return self.Product_name 

class Bio (models.Model):
    Title = models.CharField(max_length=10000)
    Biograpghy =  models.CharField(max_length=10000)
    
    
    def __str__(self):
        return self.Title

class People (models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Gender =  models.CharField(max_length=6)
    Age = models.IntegerField()
    Location = models.ForeignKey(Address, on_delete=models.CASCADE)
    Medical = models.ManyToManyField(Doctor)
    Biography = models.ForeignKey(Bio, on_delete=models.CASCADE)


    def __str__(self):
        return self.First_name