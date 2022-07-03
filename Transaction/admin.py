from django.contrib import admin

# Register your models here.
from .models import account
from .models import History

class AccountAdmin(admin.ModelAdmin):
    list_display = ('user','phone','balance')
admin.site.register(account, AccountAdmin)

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('pk','history')
admin.site.register(History, HistoryAdmin)