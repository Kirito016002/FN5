from django.db import models

class About_me(models.Model):
    text = models.TextField()
    
    class Meta():
        verbose_name = "About me"
        verbose_name_plural = "About me"


class My_equpment(models.Model):
    name = models.TextField()
    
    class Meta():
        verbose_name = "My equpment"
        verbose_name_plural = "My equpments"
        
        
class My_portfolio(models.Model):
    path = models.TextField()
    
    def __str__(self):
        return self.path
    
    class Meta():
        verbose_name = "My portfolio"
        verbose_name_plural = "My portfolio images"
        
        
class My_service(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()    
    path = models.TextField()
    
    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name = "My servics"
        verbose_name_plural = "My services"
        
    
class Massage(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    massage = models.TextField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta():
        verbose_name = "Massage"
        verbose_name_plural = "Massages"