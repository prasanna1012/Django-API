from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=10,blank=True, null= True, unique= True)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    first_name =  models.CharField(max_length=10)
    lastname =  models.CharField(max_length=10)
    password =  models.CharField(max_length=10)
    
    def __str__(self):
        return self.username

class Recipe(models.Model):
    name = models.CharField(max_length=20,blank=False, null= False, unique= True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    
class Ingredient(models.Model):
    text = models.CharField(max_length=20,blank=False, null= False, unique= True)
    recepie = models.ForeignKey(Recipe, on_delete=models.SET_NULL, null=True)

class Step(models.Model):
    step_text = models.CharField(max_length=20,blank=False, null= False, unique= True)
    recepie = models.ForeignKey(Recipe, on_delete=models.SET_NULL, null=True)
