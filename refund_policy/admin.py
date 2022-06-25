from django.contrib import admin
from .models import RefundPolicyIntroduction, OrderCancelation, DoubleCharge, ShortageOfWriter, RevisionDeadline, Quality

# Register your models here.
admin.site.register(RefundPolicyIntroduction)
admin.site.register(OrderCancelation)
admin.site.register(RevisionDeadline)
admin.site.register(Quality)
admin.site.register(ShortageOfWriter)
admin.site.register(DoubleCharge)