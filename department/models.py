from django.db import models

# Create your models here.
class Department(models.Model):

    depname = models.CharField(max_length=64)
    workid = models.IntegerField()
    topid=  models.IntegerField()

    def __str__(self):
        return self.depname

    class Meta:
        db_table = "department"