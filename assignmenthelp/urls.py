from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('',views.index_page),
    path(r'about/',views.about_view),
    path(r'samples/',views.samples),
    path(r'create_order/',views.create_order),
    path(r'dashboard/',views.dashboard,name='dashboard'),
    path(r'revision_policy/',views.revision_policy),
    path(r'refund_policy/',views.refund_policy),
    path(r'how_we_work/',views.how_we_work,name='howwework'),
    path(r'order_files/<slug>/',views.order_files),
    path(r'order_description/<slug>/',views.order_description),
    path(r'order_instructions/<slug>/',views.order_instructions),
    path('payments/',include('payments.urls')),
]
#appending the static files urls to the above media
urlpatterns += staticfiles_urlpatterns()
#how to upload media..appending the media url to the patterns above
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
