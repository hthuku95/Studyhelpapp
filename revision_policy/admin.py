from django.contrib import admin
from .models import Instruction, Introduction, Submission, Conclusion, Deadline
# Register your models here.

admin.site.register(Instruction)
admin.site.register(Introduction)
admin.site.register(Submission)
admin.site.register(Conclusion)
admin.site.register(Deadline)