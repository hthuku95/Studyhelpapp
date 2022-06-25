from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .import views

urlpatterns = [
    path('checkout/<slug>/',views.checkout_view),
    path('payment/<slug>/',views.payment_view),
    path(r'payment_complete/',views.payment_complete,name='complete')
]
