from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import HowWeWork, HowWeWorkCheckList, Faq
# Register your models here.

class FaqAdmin(admin.ModelAdmin):
    list_display = ('date','question','answer')
    list_filter = ('date',)

admin.site.register(HowWeWork)
admin.site.register(HowWeWorkCheckList)
admin.site.register(Faq,FaqAdmin)
