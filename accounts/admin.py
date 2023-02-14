from django.contrib import admin

from .models import User, WhitelistDomains, WhitelistEmails

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    
    list_display = ("id", "username" ,"last_name", "first_name")

admin.site.register(WhitelistDomains)
admin.site.register(WhitelistEmails)
