from django.contrib import admin
from .models import Account
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'date_joined', 'last_login', 'first_name', 'last_name', 'is_active']
    list_display_links = ['email', 'username','first_name', 'last_name']
    readonly_fields = ['date_joined', 'last_login']
    ordering = ['-date_joined']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)