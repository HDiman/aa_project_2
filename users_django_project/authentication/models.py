from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField('Username', max_length=50)
    first_name = models.CharField('First Name', max_length=250)
    last_name = models.CharField('Last Name', max_length=250)
    email = models.CharField('Email', max_length=250)
    password = models.CharField('Password', max_length=250)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
