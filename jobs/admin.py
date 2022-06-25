from django.contrib import admin
from .models import Order, Sample, Writer, OrderFile
from django.contrib.auth.models import Group

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('reference_code',
                    'email',
                    'payment_complete',
                    'status',
                    'academic_level',
                    'subject',
                    'number_of_pages',
                    'line_spacing',
                    'days',
                    'type',
                    'paper_format',
                    'price',
                    'writer')

    list_filter = ('email','subject','payment_complete','status','writer')

class SampleAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'no_of_pages',
                    'format',
                    'subject')

class WriterAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'phone'
                         )

class OrderFileAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'file',
                    'order'
                         )
    list_filter = ('order',)


admin.site.register(Order,OrderAdmin)
admin.site.register(Sample,SampleAdmin)
admin.site.register(Writer,WriterAdmin)
admin.site.register(OrderFile,OrderFileAdmin)


admin.site.site_header = "Assignment Hub Admin"