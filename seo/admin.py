from django.contrib import admin
from .models import AboutMetaField,AboutTitleField,SampleMetaField,SampleTitleField,IndexMetaField,IndexTitleField,PrivacypolicyMetaField,PrivacypolicyTitleField,OrderMetaField,OrderTitleField,DashboardMetaField,DashboardTitleField
# Register your models here.

admin.site.register(AboutMetaField)
admin.site.register(AboutTitleField)
admin.site.register(SampleMetaField)
admin.site.register(SampleTitleField)
admin.site.register(IndexMetaField)
admin.site.register(IndexTitleField)
admin.site.register(OrderMetaField)
admin.site.register(OrderTitleField)
admin.site.register(DashboardMetaField)
admin.site.register(DashboardTitleField)