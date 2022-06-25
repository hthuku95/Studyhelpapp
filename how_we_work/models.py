from django.db import models

# Create your models here.
from django.db import models

def save_one_only(model_name):
    def save(self, *args, **kwargs):
        if not self.pk and model_name.objects.exists():
        # if you'll not check for self.pk 
        # then error will also raised in update of exists model
            raise ValidationError('There is can be only one '+model_name+' instance')
        return super(model_name, self).save(*args, **kwargs)

# Create your models here.
class HowWeWork(models.Model):
    id = models.AutoField(primary_key=True)
    introduction = models.TextField()
    body = models.TextField(blank=True,null=True)
    date = models.DateField(auto_now_add=True)
    thumbnail = models.FileField(blank=True,null=True)

    save_one_only('HowWeWork')

    def __str__(self):
        return self.introduction[:50]

class HowWeWorkCheckList(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name   

class Faq(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField( max_length=256)
    answer = models.TextField()
    date = models.DateField(auto_now_add=True, blank=True,null=True)

    def __str__(self):
        return self.question
    