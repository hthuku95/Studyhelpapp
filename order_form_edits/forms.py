from django import forms
from django.forms import MultipleChoiceField, ChoiceField
import random
from .models import Page,Spacing,Subject,Format,Day,Type,AcademicLevel
# Create your views here.
#choice Lists
SUBJECT_CHOICES = []
PAGE_CHOICES = []
ACADEMIC_CHOICES = []
SPACING_CHOICES = []
FORMAT_CHOICES = []
DAY_CHOICES = []
TYPE_CHOICES = []

page_choices = Page.objects.all()
academic_choices = AcademicLevel.objects.all()
spacing_choices = Spacing.objects.all()
format_choices = Format.objects.all()
subject_choices = Subject.objects.all()
day_choices = Day.objects.all()
type_choices = Type.objects.all()

for page in page_choices:
    PAGE_CHOICES.append((page.name[:2],page.name))

PAGE_CHOICES = tuple(PAGE_CHOICES)

for academic in academic_choices:
    ACADEMIC_CHOICES.append((academic.name[:2],academic.name))

ACADEMIC_CHOICES = tuple(ACADEMIC_CHOICES)

for spacing in spacing_choices:
    SPACING_CHOICES.append((spacing.name[:2],spacing.name))

SPACING_CHOICES = tuple(SPACING_CHOICES)

for format in format_choices:
    FORMAT_CHOICES.append((format.name[:2],format.name))

FORMAT_CHOICES = tuple(FORMAT_CHOICES)

for subject in subject_choices:
    SUBJECT_CHOICES.append((subject.name[:2],subject.name))

SUBJECT_CHOICES = tuple(SUBJECT_CHOICES)

for day in day_choices:
    DAY_CHOICES.append((day.name[:2],day.name))

DAY_CHOICES = tuple(DAY_CHOICES)

for type in type_choices:
    TYPE_CHOICES.append((type.name[:2],type.name))

TYPE_CHOICES = tuple(TYPE_CHOICES)

class OrderForm(forms.Form):
    name = forms.CharField(label='', max_length=100,widget=forms.TextInput)
    email = forms.EmailField( label='',max_length=100 ,widget=forms.EmailInput)
    academiclevel = MultipleChoiceField(label='', widget=forms.SelectMultiple,choices=ACADEMIC_CHOICES)
    subject = MultipleChoiceField(label='', widget=forms.SelectMultiple,choices=SUBJECT_CHOICES)
    pages = MultipleChoiceField(label='', widget=forms.SelectMultiple,choices=PAGE_CHOICES)
    linespacing = MultipleChoiceField(label='',widget=forms.SelectMultiple,choices=SPACING_CHOICES)
    days = MultipleChoiceField(label='', widget=forms.SelectMultiple,choices=DAY_CHOICES)
    type = MultipleChoiceField(label='', widget=forms.SelectMultiple,choices=TYPE_CHOICES)
    format = MultipleChoiceField(label='', widget=forms.SelectMultiple,choices=FORMAT_CHOICES)

    
    instructions = forms.CharField( label='',widget=forms.Textarea(attrs={'rows':6,
                                                                            'place-holder':'Instructions...'
                                                                            }))

class OrderFileForm(forms.Form):
    docfile = forms.FileField(label='', max_length=100, required=False)