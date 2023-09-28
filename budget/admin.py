from django.contrib import admin
from .models import Budget, BudgetPeriod, Month, Year

admin.site.register([Budget, BudgetPeriod, Month, Year])
