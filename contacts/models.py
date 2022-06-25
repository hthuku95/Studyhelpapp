from django.db import models
from django.conf import settings
from jobs.models import Order

# Create your models here.
#contact model

def save_one_only(model_name):
    def save(self, *args, **kwargs):
        if not self.pk and model_name.objects.exists():
        # if you'll not check for self.pk 
        # then error will also raised in update of exists model
            raise ValidationError('There is can be only one '+model_name+' instance')
        return super(model_name, self).save(*args, **kwargs)

class Contact (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    #snippet utils
    def __str__(self):
        return self.name

    
    def text(self):
        return self.message[:50]

class Whatsapp (models.Model):
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=50)

    save_one_only("Whatsapp")

    def __str__(self):
        return self.number
    
        

class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order, blank=True)

    def __str__(self):
        return self.user.username
    
