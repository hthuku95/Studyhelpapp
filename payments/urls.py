from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .import views

app_name = 'payment'

urlpatterns = [
    path('checkout/<slug>/',views.checkout_view),
    path('payment/<slug>/',views.payment_view),
    path(r'payment_complete/<slug>/',views.payment_complete,name='complete'),
]
