from django.contrib import admin
from .models import Account

class AccountAdmin(admin.ModelAdmin):
    search_fields = ['username']


admin.site.register(Account, AccountAdmin)