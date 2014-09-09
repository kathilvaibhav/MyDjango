from django.db import models
# Create your models here.
from django.utils.encoding import smart_unicode
class SignUp(models.Model):
    first_name = models.CharField(max_length=120,null=True,blank=True)
    last_name = models.CharField(max_length=120,null=True,blank=True)
    email=models.EmailField()
    
    def __unicode__(self):
        return smart_unicode(self.email)