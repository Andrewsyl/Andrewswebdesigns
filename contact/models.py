from django.db import models
from django.utils import timezone


# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=250)
    #topic = models.CharField(max_length=200)
    message = models.TextField(max_length=900)
    timestamp = models.DateTimeField(default=timezone.now)  # good to use timestamp for records
    #image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-timestamp']
