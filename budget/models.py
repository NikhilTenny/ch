from django.db import models

from category.models import UserCategory
from user.models import Users

class Month(models.Model):
    name = models.CharField(max_length=20, 
            unique=True, null=False, verbose_name="Month Name",) # Eg: 'Jan', 'Feb', 'Mar'
    short_name = models.CharField(max_length=4, 
            unique=True, null=False)
    month_index = models.IntegerField(unique=True, null=False) 
    
class Year(models.Model):
    year = models.IntegerField(null=False, unique=True)  

class Budget(models.Model):
    category_id = models.ForeignKey(UserCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    
    

