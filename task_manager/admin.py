from django.contrib import admin
from .models import admin_task

# Register your models here.
for admin_model in admin_task:
    admin.site.register(admin_model)
