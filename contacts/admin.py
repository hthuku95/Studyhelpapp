from django.contrib import admin

# Register your models here.
from .models import Contact,UserProfile,Whatsapp


class ContactAdmin(admin.ModelAdmin):
    list_display = ('date','name','email','text')
    list_filter = ('date','email')

admin.site.register(Contact, ContactAdmin)
admin.site.register(Whatsapp)