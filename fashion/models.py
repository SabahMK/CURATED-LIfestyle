from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
def upload_image(instance, filename):
    return f'{instance.user}/{filename}'

def upload(instance,filename):
    return f'{instance.title}/{filename}'

class Fashion(models.Model):
    image1 = models.ImageField(_("Image"), upload_to=upload,blank=True , null=True)
    title = models.CharField(_("Title"), max_length=50 ,blank=True , null=True)

    def __str__(self):
        return f'{self.title}'

    

class Message(models.Model):
    post = models.ForeignKey(Fashion, verbose_name=_("Post"), on_delete=models.CASCADE, blank=True, null=True)
    user = models.CharField(_("User"), max_length=50, blank=True , null=True)
    message = models.TextField(_('Message'), blank=True , null=True)
    image2 = models.ImageField(_("Image1"), upload_to=upload_image,blank=True , null=True)


    
    def __str__(self):
        return f'{self.user}'

    
