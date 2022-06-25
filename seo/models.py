from django.db import models

def save_one_only(model_name):
    def save(self, *args, **kwargs):
        if not self.pk and model_name.objects.exists():
        # if you'll not check for self.pk 
        # then error will also raised in update of exists model
            raise ValidationError('There is can be only one '+model_name+' instance')
        return super(model_name, self).save(*args, **kwargs)

# Create your models here.

# title fields
# about
class AboutTitleField(models.Model):
    id = models.AutoField(primary_key=True)
    title_description = models.CharField( max_length=100)

    save_one_only("AboutTitleField")

    def __str__(self):
        return self.title_description
    
# create order
class OrderTitleField(models.Model):
    id = models.AutoField(primary_key=True)
    title_description = models.CharField( max_length=100)

    save_one_only("OrderTitleField")

    def __str__(self):
        return self.title_description

# dashboard
class DashboardTitleField(models.Model):
    id = models.AutoField(primary_key=True)
    title_description = models.CharField( max_length=100)

    save_one_only("DashboardTitleField")

    def __str__(self):
        return self.title_description

# index
class IndexTitleField(models.Model):
    id = models.AutoField(primary_key=True)
    title_description = models.CharField( max_length=100)

    save_one_only("IndexTitleField")

    def __str__(self):
        return self.title_description

# privacy_policy
class PrivacypolicyTitleField(models.Model):
    id = models.AutoField(primary_key=True)
    title_description = models.CharField( max_length=100)

    save_one_only("PrivacypolicyTitleField")

    def __str__(self):
        return self.title_description

# samples
class SampleTitleField(models.Model):
    id = models.AutoField(primary_key=True)
    title_description = models.CharField( max_length=100)

    save_one_only("SampleTitleField")

    def __str__(self):
        return self.title_description

# Meta fields 
# about
class AboutMetaField(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    keywords = models.TextField()

    save_one_only("AboutMetaField")

    def __str__(self):
        return self.description
    

# create order
class OrderMetaField(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    keywords = models.TextField()

    save_one_only("OrderMetaField")

    def __str__(self):
        return self.description
    

# dashboard
class DashboardMetaField(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    keywords = models.TextField()

    save_one_only("DashboardMetaField")

    def __str__(self):
        return self.description

# index
class IndexMetaField(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    keywords = models.TextField()

    save_one_only("IndexMetaField")

    def __str__(self):
        return self.description

# privacy policy
class PrivacypolicyMetaField(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    keywords = models.TextField()

    save_one_only("PrivacypolicyMetaField")

    def __str__(self):
        return self.description
# samples
class SampleMetaField(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    keywords = models.TextField()

    save_one_only("SampleMetaField")

    def __str__(self):
        return self.description

