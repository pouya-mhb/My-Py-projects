from django.db import models

# Create your models here.
class Contact(models.Model):
  
    first_name = models.CharField(max_length=100, verbose_name='اسم')
    last_name = models.CharField(max_length=100, verbose_name='فامیلی')
    email = models.EmailField(max_length=254,verbose_name='رایانامه')
    phone = models.CharField(verbose_name='تلفن',max_length=15)
    description = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    #defines string represention of oject 
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
