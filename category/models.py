from django.db import models

from user.models import Users

class Category(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    parent_id = models.ForeignKey('self', 
            null=True, blank=True, on_delete=models.CASCADE)
     
    def __str__(self):
        return self.name
    
class UserCategory(models.Model):
    name = models.CharField(max_length=80,  null=False, blank=False)
    parent_id = models.ForeignKey('self', 
            null=True, blank=True, on_delete=models.CASCADE)
    main_category_id = models.ForeignKey(Category, 
            null=True, blank=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users,  
            null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

