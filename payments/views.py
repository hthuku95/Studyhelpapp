from django.shortcuts import render, HttpResponse, redirect, \
    get_object_or_404, reverse
from django.views.generic import ListView,DetailView,View
from django.contrib import messages
from django import forms

from django.conf import settings
from decimal import Decimal
from .models import Payment,Address
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import CheckoutForm

from django.contrib import messages
from contacts.models import Whatsapp
from page_edits.models import GmailLink,InstagramAccount,TwitterAccount,FacebookAccount,PhoneNumber
from jobs.models import Order

import random
import string

# Create your views here.
#checkout view
def create_charge_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))

@login_required()
def checkout_view(request,slug):

    order = Order.objects.get(reference_code=slug)
    gmail_links = GmailLink.objects.all()
    instagram_accounts = InstagramAccount.objects.all()
    fb_accounts = FacebookAccount.objects.all()
    twitter_accounts = TwitterAccount.objects.all()
    phone_numbers = PhoneNumber.objects.all()
    whatsapp = Whatsapp.objects.all()

    context = {
                'gmail_links':gmail_links,
                'instagram_accounts':instagram_accounts,
                'fb_accounts':fb_accounts,
                'twitter_accounts':twitter_accounts,
                'phone_numbers':phone_numbers,
                'whatsapp':whatsapp,
                'order':order,
              }

    billing_address_qs = Address.objects.filter(
        user=request.user,
        default=True
    )
    if billing_address_qs.exists():
        context.update(
            {'default_billing_address': billing_address_qs[0]})
    

    if request.method == 'POST':
        form =CheckoutForm(request.POST)
        if form.is_valid():
            use_default_billing = form.cleaned_data.get(
                    'use_default_billing')

            if use_default_billing:
                print("Using the defualt billing address")
                address_qs = Address.objects.filter(
                    user=request.user,
                    default=True
                )
                if address_qs.exists():
                    billing_address = address_qs[0]
                    order.billing_address = billing_address
                    order.save()

                    messages.success(request,"Complete your payment first, for you to download your Assignment!")
                    return redirect('/payments/payment/'+order.reference_code+'/')
                else:
                    messages.warning(
                        request, "No default billing address available")
                    return redirect('/payments/checkout/'+order.reference_code+'/')
            else:
                # User is entering a new billing Address
                m_billing_address = form.cleaned_data['billing_address']
                m_billing_address2 = form.cleaned_data['billing_address2']
                m_billing_zip = form.cleaned_data['billing_zip']
                m_first_name = form.cleaned_data['first_name']
                m_last_name = form.cleaned_data['last_name']

                try:
                    user = request.user

                    if user.first_name and user.last_name:
                        address = Address(
                                    user = request.user,
                                    street_address=m_billing_address,
                                    apartment_address=m_billing_address2,
                                    first_name=m_first_name,
                                    last_name=m_last_name,
                                    zip=m_billing_zip)
                        address.save()
                    else:
                        user.first_name = m_first_name
                        user.save()
                        user.last_name = m_last_name
                        user.save()

                        address = Address(
                                    user = request.user,
                                    street_address=m_billing_address,
                                    apartment_address=m_billing_address2,
                                    first_name=m_first_name,
                                    last_name=m_last_name,
                                    zip=m_billing_zip)
                        address.save()

                    # Setting default billing address
                    set_default_billing = form.cleaned_data.get(
                            'set_default_billing')

                    if set_default_billing:
                        address.default = True
                        address.save()
                        
                    order.billing_address = address
                    order.save()

                    messages.success(request,"Billing address saved succesfully. Complete payment!")
                    return redirect('/payments/payment/'+order.reference_code+'/')

                except Exception as e:
                    messages.warning(request,"Please enter all the required fields")
                    print(e)
                    return redirect('/payments/checkout/'+order.reference_code+'/')
        else:
            messages.warning(request,"Plese complete all the required fields")
            print("exception occured or something")
            return redirect('/payments/checkout/'+order.reference_code+'/')
    else:
        form = CheckoutForm()
        context.update({
            'form':form
        })
    messages.success(request, "Complete your payment first, for you to download your Assignment!")
    return render(request,'payments/checkout.htm',context)

@login_required()
def payment_view(request,slug):
    order = Order.objects.get(reference_code=slug)

    gmail_links = GmailLink.objects.all()
    instagram_accounts = InstagramAccount.objects.all()
    fb_accounts = FacebookAccount.objects.all()
    twitter_accounts = TwitterAccount.objects.all()
    phone_numbers = PhoneNumber.objects.all()
    whatsapp = Whatsapp.objects.all()

    
    context = {
                'gmail_links':gmail_links,
                'instagram_accounts':instagram_accounts,
                'fb_accounts':fb_accounts,
                'twitter_accounts':twitter_accounts,
                'phone_numbers':phone_numbers,
                'whatsapp':whatsapp,
                'order':order,
              }
    return render(request,'payments/payment.htm',context)


def payment_complete(request,slug):
    order = Order.objects.get(reference_code=slug)

    order.payment_complete = 'T'
    order.save()

    charge = create_charge_id()
    charge = charge.upper()

    payment = Payment(
        charge_id=charge,
        user=order.user,
        amount=order.price
    )
    payment.save()

    order.payment = payment
    order.save()

    messages.success(request,"Payment for your order has been completed Successfully")
    return redirect("dashboard")
