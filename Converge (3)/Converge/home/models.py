from django.db import models

class Search(models.Model):
    query = models.CharField(max_length=255)
class Search(models.Model):
    username = models.CharField(max_length=255)
    project_title = models.CharField(max_length=255)
    project_description = models.TextField()
    file = models.FileField(upload_to='files/')
    min_price = models.IntegerField()
    max_price = models.IntegerField()
class login(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
class signup(models.Model):
    username = models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    email=models.EmailField(max_length=25)
    confpassword=models.CharField(max_length=255)
    Contactnumber=models.CharField(max_length=15)
    country=models.CharField(max_length=355)
class seller(models.Model):
    username = models.CharField(max_length=255)
