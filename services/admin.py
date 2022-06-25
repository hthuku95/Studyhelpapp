from django.contrib import admin
from .models import AssignmentWritingService, ProofReadingService, DissertationAndThesisHelp, ContentWritingService
# Register your models here.

class AssignmentWritingServiceAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'title',
        'body'
    )

class ProofReadingServiceAdmin(admin.ModelAdmin):
        list_display = (
        'date',
        'title',
        'body'
    )

class DissertationAndThesisHelpAdmin(admin.ModelAdmin):
        list_display = (
        'date',
        'title',
        'body'
    )

class ContentWritingServiceAdmin(admin.ModelAdmin):
        list_display = (
        'date',
        'title',
        'body'
    )

admin.site.register(AssignmentWritingService,AssignmentWritingServiceAdmin)
admin.site.register(ProofReadingService,ProofReadingServiceAdmin)
admin.site.register(DissertationAndThesisHelp,DissertationAndThesisHelpAdmin)
admin.site.register(ContentWritingService,ContentWritingServiceAdmin)
