from django.contrib import admin

from category.models import Category, UserCategory

admin.site.register([Category, UserCategory])
