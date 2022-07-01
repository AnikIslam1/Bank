from django.contrib import admin

# Register your models here.
from .models import customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance')
admin.site.register(customer, CustomerAdmin)