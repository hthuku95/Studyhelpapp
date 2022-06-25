from django.contrib import admin
from .models import Format,Type,Day,Spacing,Subject,AcademicLevel,Page

# Register your models here.
admin.site.register(Format)
admin.site.register(Type)
admin.site.register(Day)
admin.site.register(Spacing)
admin.site.register(AcademicLevel)
admin.site.register(Subject)
admin.site.register(Page)