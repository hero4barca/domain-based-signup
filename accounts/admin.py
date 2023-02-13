from django.contrib import admin

from .models import User, WhitelistDomains, WhitelistEmails

# Register your models here.
admin.site.register(User)
admin.site.register(WhitelistDomains)
admin.site.register(WhitelistEmails)
