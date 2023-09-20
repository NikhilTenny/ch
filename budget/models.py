from django.db import models

from category.models import UserCategory

class Month(models.Model):
    name = models.CharField(max_length=20, 
            unique=True, null=False, verbose_name="Month Name",) # Eg: 'Jan', 'Feb', 'Mar'
    short_name = models.CharField(max_length=4, 
            unique=True, null=False)
    month_index = models.IntegerField(unique=True, null=False) 
    
class Year(models.Model):
    year = models.IntegerField(null=False, unique=True)  

class Budget(models.Model):
    category = models.ForeignKey(UserCategory, bla)
    
    

