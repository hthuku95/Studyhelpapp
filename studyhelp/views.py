from django.shortcuts import render,redirect
from .forms import ContactForm
from order_form_edits.forms import OrderForm,OrderFileForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from contacts.models import Contact, UserProfile,Whatsapp
from jobs.models import Order, Sample, OrderFile,Writer
from how_we_work.models import Faq, HowWeWork, HowWeWorkCheckList
from refund_policy.models import RefundPolicyIntroduction, OrderCancelation, DoubleCharge, ShortageOfWriter, RevisionDeadline, Quality
from revision_policy.models import Instruction, Introduction, Conclusion, Submission, Deadline
from order_form_edits.models import Page,AcademicLevel,Spacing,Format,Subject,Day,Type
from seo.models import AboutMetaField,AboutTitleField,SampleMetaField,SampleTitleField,IndexMetaField,IndexTitleField,PrivacypolicyMetaField,PrivacypolicyTitleField,OrderMetaField,OrderTitleField,DashboardMetaField,DashboardTitleField
from page_edits.models import HomeHeader,HowWeWorkCheckListItem,HowWeWorkText,BrandName,Address,GmailLink,InstagramAccount,TwitterAccount,FacebookAccount,PhoneNumber,AboutPage
from order_form_edits.forms import ACADEMIC_CHOICES,SPACING_CHOICES,SUBJECT_CHOICES,TYPE_CHOICES,FORMAT_CHOICES,DAY_CHOICES,PAGE_CHOICES
from django.contrib import messages
from services.models import AssignmentWritingService, DissertationAndThesisHelp, ProofReadingService, ContentWritingService
import random
import string
import smtplib

def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))

def index_page(request):

    headers = HomeHeader.objects.all().order_by('date')
    how_we_work_texts = HowWeWork.objects.all()
    brands = BrandName.objects.all()
    samples = Sample.objects.all()
    addresses = Address.objects.all()
    gmail_links = GmailLink.objects.all()
    instagram_accounts = InstagramAccount.objects.all()
    fb_accounts = FacebookAccount.objects.all()
    twitter_accounts = TwitterAccount.objects.all()
    phone_numbers = PhoneNumber.objects.all()
    abouts = AboutPage.objects.all()
    whatsapp = Whatsapp.objects.all()

    index_title = IndexTitleField.objects.all()
    index_meta = IndexMetaField.objects.all()

    dissertations = DissertationAndThesisHelp.objects.all()
    assignments = AssignmentWritingService.objects.all()
    proofreadings = ProofReadingService.objects.all()
    contents = ContentWritingService.objects.all()
    
    context = {
                'headers':headers,
                'how_we_work_texts':how_we_work_texts,
                'brands':brands,
                'samples':samples,
                'addresses':addresses,
                'gmail_links':gmail_links,
                'instagram_accounts':instagram_accounts,
                'fb_accounts':fb_accounts,
                'twitter_accounts':twitter_accounts,
                'phone_numbers':phone_numbers,
                'dissertations':dissertations,
                'proofreadings':proofreadings,
                'contents':contents,
                'assignments':assignments,
                'whatsapp':whatsapp,
                'index_title':index_title,
                'index_meta':index_meta
              }

    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            
            #getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
        
            try:
                contact = Contact(name=m_name,email=email_address,message=mail_message)
                contact.save()

                messages.success(request,"Message sent succesfully.")
                return redirect('/')

            except Exception as e:
                messages.warning(request,"Please enter all the required fields")
                return redirect('/')
        else:
            messages.warning(request,"Plese complete all the required fields")
            return redirect('/')
    else:
        form = ContactForm()
        context.update({
            'form':form
        })
    return render(request,'index.htm',context)

#about view
def about_view(request):

    samples = Sample.objects.all()
    addresses = Address.objects.all()
    gmail_links = GmailLink.objects.all()
    instagram_accounts = InstagramAccount.objects.all()
    fb_accounts = FacebookAccount.objects.all()
    twitter_accounts = TwitterAccount.objects.all()
    phone_numbers = PhoneNumber.objects.all()
    abouts = AboutPage.objects.all()
    whatsapp = Whatsapp.objects.all()
    questions = Faq.objects.all()
    about_title = AboutTitleField.objects.all()
    about_meta = AboutMetaField.objects.all()

    context = {
                'samples':samples,
                'addresses':addresses,
                'gmail_links':gmail_links,
                'instagram_accounts':instagram_accounts,
                'fb_accounts':fb_accounts,
                'twitter_accounts':twitter_accounts,
                'phone_numbers':phone_numbers,
                'abouts':abouts,
                'questions':questions,
                'whatsapp':whatsapp,
                'about_title':about_title,
                'about_meta':about_meta
              }

    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            
            #getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
        
            try:
                contact = Contact(name=m_name,email=email_address,message=mail_message)
                contact.save()

                messages.success(request,"Message sent succesfully.")
                return redirect('/about/')

            except Exception as e:
                messages.warning(request,"Please enter all the required fields")
                return redirect('/about/')
        else:
            messages.warning(request,"Plese complete all the required fields")
            return redirect('/about/')
    else:
        form = ContactForm()
        context.update({
            'form':form
        })
    return render(request,'about.htm',context)


@login_required()
def order_files(request,slug):
    order = Order.objects.get(reference_code=slug)
    headers = HomeHeader.objects.all().order_by('date')
    how_we_work_texts = HowWeWork.objects.all()
    addresses = Address.objects.all()
    gmail_links = GmailLink.objects.all()
    instagram_accounts = InstagramAccount.objects.all()
    fb_accounts = FacebookAccount.objects.all()
    twitter_accounts = TwitterAccount.objects.all()
    phone_numbers = PhoneNumber.objects.all()
    whatsapp = Whatsapp.objects.all()
    order_title = OrderTitleField.objects.all()
    order_meta = OrderMetaField.objects.all()
    user = request.user

    context = {
        'order':order,
        'headers':headers,
        'how_we_work_texts':how_we_work_texts,
        'addresses':addresses,
        'gmail_links':gmail_links,
        'instagram_accounts':instagram_accounts,
        'fb_accounts':fb_accounts,
        'twitter_accounts':twitter_accounts,
        'phone_numbers':phone_numbers,
        'whatsapp':whatsapp,
        'order_title':order_title,
        'order_meta':order_meta,
        'user':user,
    }

    if request.method == 'POST':
        form = OrderFileForm(request.POST,request.FILES)

        if form.is_valid():

            doc = request.FILES #returns a dict-like object
            m_file = doc['docfile']
            m_file_name = "File: "+order.reference_code+""
            try:
                #REVISIT THIS
                file = OrderFile(name= m_file_name,file=m_file,order=order)
                file.save()

                messages.success(request,"File uploaded successfully")
                return redirect('/order_files/'+order.reference_code+'/')
            except Exception as e:
                messages.warning(request,'An error occured while uploading the file. Please try again')
                print(e)
                return redirect('/order_files/'+order.reference_code+'/')
        else:
            messages.warning(request,'An error occured while uploading the file. Please try again')
            return redirect('/order_files/'+order.reference_code+'/')
    else:
        form = OrderFileForm()
        context.update(
            {'form':form}
        )
    return render(request,'order_files.htm',context)
    

@login_required()
def create_order(request):
    headers = HomeHeader.objects.all().order_by('date')
    brands = BrandName.objects.all()
    how_we_work_texts = HowWeWork.objects.all()
    addresses = Address.objects.all()
    gmail_links = GmailLink.objects.all()
    instagram_accounts = InstagramAccount.objects.all()
    fb_accounts = FacebookAccount.objects.all()
    twitter_accounts = TwitterAccount.objects.all()
    phone_numbers = PhoneNumber.objects.all()
    steps = HowWeWorkCheckList.objects.all()
    whatsapp = Whatsapp.objects.all()
    order_title = OrderTitleField.objects.all()
    order_meta = OrderMetaField.objects.all()
    user = request.user

    context = {
        'headers':headers,
        'brands':brands,
        'how_we_work_texts':how_we_work_texts,
        'addresses':addresses,
        'gmail_links':gmail_links,
        'instagram_accounts':instagram_accounts,
        'fb_accounts':fb_accounts,
        'twitter_accounts':twitter_accounts,
        'phone_numbers':phone_numbers,
        'steps':steps,
        'whatsapp':whatsapp,
        'order_title':order_title,
        'order_meta':order_meta,
        'user':user,
    }

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            m_name = form.cleaned_data['name']
            m_email = form.cleaned_data['email']

            m_academiclevel = form.cleaned_data['academiclevel']
            m_subject = form.cleaned_data['subject']
            m_pages = form.cleaned_data['pages']
            m_days = form.cleaned_data['days']
            m_spacing = form.cleaned_data['linespacing']
            m_type = form.cleaned_data['type']
            m_format = form.cleaned_data['format']

            m_instructions = form.cleaned_data['instructions']


            #refrence code and status
            
            m_status='IP'
            ref_code = create_ref_code()
            ref_code = ref_code.upper()

            # grabs the gmail link from the page edits 
            # sends email notification to it
            # subject == ref_code && body == instructions

            order = Order(name=m_name,
                            email=m_email,
                            academic_level=m_academiclevel[0],
                            subject=m_subject[0],
                            number_of_pages=m_pages[0],
                            days=m_days[0],
                            type=m_type[0],
                            line_spacing=m_spacing[0],
                            paper_format=m_format[0],
                            instructions=m_instructions,
                            status=m_status,
                            user=request.user,
                            reference_code=ref_code)
            order.save()

            messages.success(request,'Your order was created succesfully')
            messages.success(request,'Please copy the reference code and send it to our official email address or whatsapp number for more communication')
            messages.success(request,'You can acces our Whatsapp account through the floating button below')
            return redirect('/dashboard/')
        else:
            messages.warning(request,'Please enter all te required fields')
            return redirect('/create_order/')
    else:
        form = OrderForm()
        context.update(
            {'form':form}
        )
    return render(request,'create_order.htm',context)

def samples(request):
    samples = Sample.objects.all()
    headers = HomeHeader.objects.all().order_by('date')
    brands = BrandName.objects.all()
    whatsapp = Whatsapp.objects.all()
    addresses = Address.objects.all()
    gmail_links = GmailLink.objects.all()
    instagram_accounts = InstagramAccount.objects.all()
    fb_accounts = FacebookAccount.objects.all()
    twitter_accounts = TwitterAccount.objects.all()
    phone_numbers = PhoneNumber.objects.all()
    sample_title = SampleTitleField.objects.all()
    sample_meta = SampleMetaField.objects.all()


    context = {
            'samples':samples,
            'headers':headers,
            'brands':brands,
            'whatsapp':whatsapp,
            'phone_numbers':phone_numbers,
            'gmail_links':gmail_links,
            'instagram_accounts':instagram_accounts,
            'fb_accounts':fb_accounts,
            'twitter_accounts':twitter_accounts,
            'addresses':addresses,
            'sample_title':sample_title,
            'sample_meta':sample_meta
        }

    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            
            #getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
        
            try:
                contact = Contact(name=m_name,email=email_address,message=mail_message)
                contact.save()

                messages.success(request,"Message sent succesfully.")
                return redirect('/samples/')

            except Exception as e:
                messages.warning(request,"Please enter all the required fields")
                return redirect('/samples/')
        else:
            messages.warning(request,"Plese complete all the required fields")
            return redirect('/samples/')
    else:
        form = ContactForm()
        context.update({
            'form':form
        })
    return render(request,"samples.htm",context)

@login_required()
def dashboard(request):
    headers = HomeHeader.objects.all().order_by('date')
    brands = BrandName.objects.all()
    addresses = Address.objects.all()
    gmail_links = GmailLink.objects.all()
    instagram_accounts = InstagramAccount.objects.all()
    fb_accounts = FacebookAccount.objects.all()
    twitter_accounts = TwitterAccount.objects.all()
    phone_numbers = PhoneNumber.objects.all()
    completed_orders = Order.objects.filter(user=request.user,status='CP').order_by('-date_created')
    current_orders = Order.objects.filter(user=request.user,status='IP').order_by('-date_created')
    whatsapp = Whatsapp.objects.all()
    dashboard_title = DashboardTitleField.objects.all()
    dashboard_meta = DashboardMetaField.objects.all()

    context = {
        'headers':headers,
        'brands':brands,
        'addresses':addresses,
        'gmail_links':gmail_links,
        'instagram_accounts':instagram_accounts,
        'fb_accounts':fb_accounts,
        'twitter_accounts':twitter_accounts,
        'phone_numbers':phone_numbers,
        'completed_orders':completed_orders,
        'current_orders':current_orders,
        'whatsapp':whatsapp,
        'dashboard_title':dashboard_title,
        'dashboard_meta':dashboard_meta
    }

    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            
            #getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
        
            try:
                contact = Contact(name=m_name,email=email_address,message=mail_message)
                contact.save()

                messages.success(request,"Message sent succesfully.")
                return redirect('/dashboard/')

            except Exception as e:
                messages.warning(request,"Please enter all the required fields")
                return redirect('/dashboard/')
        else:
            messages.warning(request,"Plese complete all the required fields")
            return redirect('/dashboard/')
    else:
        form = ContactForm()
        context.update({
            'form':form
        })
    return render(request,'dashboard.htm',context)

@login_required()
def order_description(request,slug):
    order = Order.objects.get(reference_code=slug)
    headers = HomeHeader.objects.all().order_by('date')
    brands = BrandName.objects.all()
    whatsapp = Whatsapp.objects.all()
    addresses = Address.objects.all()
    gmail_links = GmailLink.objects.all()
    instagram_accounts = InstagramAccount.objects.all()
    fb_accounts = FacebookAccount.objects.all()
    twitter_accounts = TwitterAccount.objects.all()
    phone_numbers = PhoneNumber.objects.all()
    dashboard_title = DashboardTitleField.objects.all()
    dashboard_meta = DashboardMetaField.objects.all()


    context = {
            'order':order,
            'headers':headers,
            'brands':brands,
            'whatsapp':whatsapp,
            'phone_numbers':phone_numbers,
            'gmail_links':gmail_links,
            'instagram_accounts':instagram_accounts,
            'fb_accounts':fb_accounts,
            'twitter_accounts':twitter_accounts,
            'addresses':addresses,
            'dashboard_title':dashboard_title,
            'dashboard_meta':dashboard_meta
        }
    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            
            #getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
        
            try:
                contact = Contact(name=m_name,email=email_address,message=mail_message)
                contact.save()

                messages.success(request,"Message sent succesfully.")
                return redirect('/order_description/'+order.reference_code+'/')

            except Exception as e:
                messages.warning(request,"Please enter all the required fields")
                return redirect('/order_description/'+order.reference_code+'/')
        else:
            messages.warning(request,"Plese complete all the required fields")
            return redirect('/order_description/'+order.reference_code+'/')
    else:
        form = ContactForm()
        context.update({
            'form':form
        })
    return render(request,"order_description.htm",context)


@login_required()
def order_instructions(request,slug):
    order = Order.objects.get(reference_code=slug)
    headers = HomeHeader.objects.all().order_by('date')
    brands = BrandName.objects.all()
    whatsapp = Whatsapp.objects.all()
    addresses = Address.objects.all()
    gmail_links = GmailLink.objects.all()
    instagram_accounts = InstagramAccount.objects.all()
    fb_accounts = FacebookAccount.objects.all()
    twitter_accounts = TwitterAccount.objects.all()
    phone_numbers = PhoneNumber.objects.all()
    dashboard_title = DashboardTitleField.objects.all()
    dashboard_meta = DashboardMetaField.objects.all()


    context = {
            'order':order,
            'headers':headers,
            'brands':brands,
            'whatsapp':whatsapp,
            'phone_numbers':phone_numbers,
            'gmail_links':gmail_links,
            'instagram_accounts':instagram_accounts,
            'fb_accounts':fb_accounts,
            'twitter_accounts':twitter_accounts,
            'addresses':addresses,
            'dashboard_title':dashboard_title,
            'dashboard_meta':dashboard_meta
        }
    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            
            #getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
        
            try:
                contact = Contact(name=m_name,email=email_address,message=mail_message)
                contact.save()

                messages.success(request,"Message sent succesfully.")
                return redirect('/order_instructions/'+order.reference_code+'/')

            except Exception as e:
                messages.warning(request,"Please enter all the required fields")
                return redirect('/order_instructions/'+order.reference_code+'/')
        else:
            messages.warning(request,"Plese complete all the required fields")
            return redirect('/order_instructions/'+order.reference_code+'/')
    else:
        form = ContactForm()
        context.update({
            'form':form
        })
    return render(request,"order_instructions.htm",context)

def how_we_work(request):
    
    headers = HomeHeader.objects.all().order_by('date')
    brands = BrandName.objects.all()
    addresses = Address.objects.all()
    gmail_links = GmailLink.objects.all()
    instagram_accounts = InstagramAccount.objects.all()
    fb_accounts = FacebookAccount.objects.all()
    twitter_accounts = TwitterAccount.objects.all()
    phone_numbers = PhoneNumber.objects.all()
    abouts = AboutPage.objects.all()
    whatsapp = Whatsapp.objects.all()

    questions = Faq.objects.all()
    list_items = HowWeWorkCheckList.objects.all()
    how_we_work = HowWeWork.objects.all()

    index_title = IndexTitleField.objects.all()
    index_meta = IndexMetaField.objects.all()
    
    context = {
                'headers':headers,
                'brands':brands,
                'addresses':addresses,
                'gmail_links':gmail_links,
                'instagram_accounts':instagram_accounts,
                'fb_accounts':fb_accounts,
                'list_items':list_items,
                'questions':questions,
                'how_we_work':how_we_work,
                'twitter_accounts':twitter_accounts,
                'phone_numbers':phone_numbers,
                'whatsapp':whatsapp,
                'index_title':index_title,
                'index_meta':index_meta
              }

    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            
            #getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
        
            try:
                contact = Contact(name=m_name,email=email_address,message=mail_message)
                contact.save()

                messages.success(request,"Message sent succesfully.")
                return redirect('/how_we_work/')

            except Exception as e:
                messages.warning(request,"Please enter all the required fields")
                return redirect('/how_we_work/')
        else:
            messages.warning(request,"Plese complete all the required fields")
            return redirect('/how_we_work/')
    else:
        form = ContactForm()
        context.update({
            'form':form
        })
    return render(request,'how_we_work.htm',context)
    
def revision_policy(request):
    addresses = Address.objects.all()
    gmail_links = GmailLink.objects.all()
    instagram_accounts = InstagramAccount.objects.all()
    fb_accounts = FacebookAccount.objects.all()
    twitter_accounts = TwitterAccount.objects.all()
    phone_numbers = PhoneNumber.objects.all()
    whatsapp = Whatsapp.objects.all()

    index_title = IndexTitleField.objects.all()
    index_meta = IndexMetaField.objects.all()

    introductions = Introduction.objects.all()
    conclusions = Conclusion.objects.all()
    submissions = Submission.objects.all()
    deadlines = Deadline.objects.all()
    instructions = Instruction.objects.all()

    brands = BrandName.objects.all()
    headers = HomeHeader.objects.all().order_by('date')
    
    context = {
                'addresses':addresses,
                'gmail_links':gmail_links,
                'instagram_accounts':instagram_accounts,
                'fb_accounts':fb_accounts,
                'twitter_accounts':twitter_accounts,
                'phone_numbers':phone_numbers,
                'whatsapp':whatsapp,
                'index_title':index_title,
                'index_meta':index_meta,
                'introductions':introductions,
                'conclusions':conclusions,
                'submissions':submissions,
                'deadlines':deadlines,
                'instructions':instructions,
                'brands':brands,
                'headers':headers,
              }

    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            
            #getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
        
            try:
                contact = Contact(name=m_name,email=email_address,message=mail_message)
                contact.save()

                messages.success(request,"Message sent succesfully.")
                return redirect('/revision_policy/')

            except Exception as e:
                messages.warning(request,"Please enter all the required fields")
                return redirect('/revision_policy/')
        else:
            messages.warning(request,"Plese complete all the required fields")
            return redirect('/revision_policy/')
    else:
        form = ContactForm()
        context.update({
            'form':form
        })
    return render(request,'revision_policy.htm',context)

def refund_policy(request):
    addresses = Address.objects.all()
    gmail_links = GmailLink.objects.all()
    instagram_accounts = InstagramAccount.objects.all()
    fb_accounts = FacebookAccount.objects.all()
    twitter_accounts = TwitterAccount.objects.all()
    phone_numbers = PhoneNumber.objects.all()
    whatsapp = Whatsapp.objects.all()

    index_title = IndexTitleField.objects.all()
    index_meta = IndexMetaField.objects.all()

    introductions = RefundPolicyIntroduction.objects.all()
    cancelations = OrderCancelation.objects.all()
    deadlines = RevisionDeadline.objects.all()
    qualities = Quality.objects.all()
    writers = ShortageOfWriter.objects.all()
    charges = DoubleCharge.objects.all()

    brands = BrandName.objects.all()
    headers = HomeHeader.objects.all().order_by('date')
    
    context = {
                'addresses':addresses,
                'gmail_links':gmail_links,
                'instagram_accounts':instagram_accounts,
                'fb_accounts':fb_accounts,
                'twitter_accounts':twitter_accounts,
                'phone_numbers':phone_numbers,
                'whatsapp':whatsapp,
                'index_title':index_title,
                'index_meta':index_meta,

                'introductions':introductions,
                'cancelations':cancelations,
                'qualities':qualities,
                'deadlines':deadlines,
                'writers':writers,
                'charges':charges,
                
                'brands':brands,
                'headers':headers,
              }

    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            
            #getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
        
            try:
                contact = Contact(name=m_name,email=email_address,message=mail_message)
                contact.save()

                messages.success(request,"Message sent succesfully.")
                return redirect('/refund_policy/')

            except Exception as e:
                messages.warning(request,"Please enter all the required fields")
                return redirect('/refund_policy/')
        else:
            messages.warning(request,"Plese complete all the required fields")
            return redirect('/refund_policy/')
    else:
        form = ContactForm()
        context.update({
            'form':form
        })
    return render(request,'refund_policy.htm',context)

