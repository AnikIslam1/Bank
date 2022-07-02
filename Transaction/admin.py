from django.contrib import admin

# Register your models here.
from .models import account

class AccountAdmin(admin.ModelAdmin):
    list_display = ('user','phone','balance')
admin.site.register(account, AccountAdmin)