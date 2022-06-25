from django.db import models

def save_one_only(model_name):
    def save(self, *args, **kwargs):
        if not self.pk and model_name.objects.exists():
        # if you'll not check for self.pk 
        # then error will also raised in update of exists model
            raise ValidationError('There is can be only one '+model_name+' instance')
        return super(model_name, self).save(*args, **kwargs)


# Create your models here.
class Introduction(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="Introduction")
    body = models.TextField()

    save_one_only("Introduction")

    def __str__(self):
        return self.name

class Instruction(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="Instruction")

    heading = models.CharField(max_length=50)
    body = models.TextField()

    save_one_only("Instructions")

    def __str__(self):
        return self.name

class Submission(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="Submission")

    heading = models.CharField( max_length=50)
    body = models.TextField()

    save_one_only("Submission")

    def __str__(self):
        return self.name

class Deadline(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="Deadline")

    heading = models.CharField( max_length=50)
    body = models.TextField()

    save_one_only("Deadline")

    def __str__(self):
        return self.name

class Conclusion(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="Conclusion")
    body = models.TextField()

    save_one_only("Conclusion")

    def __str__(self):
        return self.name
    
