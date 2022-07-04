from django.db import models
from django.conf import settings
from order_form_edits.forms import ACADEMIC_CHOICES,SPACING_CHOICES,SUBJECT_CHOICES,TYPE_CHOICES,FORMAT_CHOICES,DAY_CHOICES,PAGE_CHOICES

STATUS_CHOICES = (
    ('IP', 'inprogress'),
    ('CP', 'Completed'),
    ('CN', 'Cancelled'),
)
PAYMENT_COMPLETE_CHOICES = (
    ('T', 'True'),
    ('F', 'False'),
)

# Create your models here.
class Writer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,blank=True,null=True)
    phone = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    #refrence code
    reference_code = models.CharField(max_length=50,blank=True,null=True)
    
    #meta
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    academic_level = models.CharField(choices=ACADEMIC_CHOICES,max_length=2, blank=True, null=True)
    subject = models.CharField(choices=SUBJECT_CHOICES,max_length=2, blank=True, null=True)
    number_of_pages = models.CharField(choices=PAGE_CHOICES,max_length=2, blank=True, null=True)
    line_spacing = models.CharField(choices=SPACING_CHOICES,max_length=2, blank=True, null=True)
    days = models.CharField(choices=DAY_CHOICES, max_length=2, blank=True, null=True)
    type = models.CharField(choices=TYPE_CHOICES,max_length=2, blank=True, null=True)
    paper_format = models.CharField(choices=FORMAT_CHOICES, max_length=2, blank=True, null=True)
    instructions = models.TextField(default="")

    #assignment file
    assignment_file = models.FileField( max_length=100, blank=True, null=True)

    #price field
    price = models.FloatField(blank=True,null=True)

    #order status
    status = models.CharField(choices=STATUS_CHOICES,max_length=2,blank=True,null=True)

    #date fields
    date_created = models.DateTimeField(auto_now_add=True)

    #user field
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, blank=True,null=True)

    #boolean fields
    payment_complete = models.CharField(max_length=1,choices=PAYMENT_COMPLETE_CHOICES,blank=True,null=True,default="F")

    #file field
    writer =  models.ForeignKey(Writer,  on_delete=models.CASCADE, blank=True,null=True)

    def __str__(self):
        return self.reference_code

    def snippet(self):
        return self.instructions[:50]


class OrderFile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True,null=True,max_length=50)
    file = models.FileField(max_length=100,blank=True,null=True)
    order = models.ForeignKey(Order, blank=True,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Sample(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField( max_length=50)
    description = models.TextField(blank=True)
    no_of_pages = models.IntegerField(blank=True,null=True)
    format = models.CharField(max_length=50,blank=True,null=True)
    subject = models.CharField(max_length=50,blank=True,null=True)
    file = models.FileField(max_length=100,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.description[:50]

