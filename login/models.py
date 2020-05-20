from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=64, verbose_name='username')
    password = models.CharField(max_length=63, null=True, verbose_name='password')
    role = models.CharField(max_length=10, null=True, verbose_name='role')

    def __str__(self):
        return self.username
    class Meta:
        db_table = "user"
class Department(models.Model):
    depname = models.CharField(max_length=64, verbose_name='depname')
    workid = models.IntegerField(max_length=64, verbose_name='workid')
    topid = models.IntegerField(max_length=64, verbose_name='topid')
    def __str__(self):
        return self.depname
    class Meta:
        db_table = "u_deppartment"