from django.db import models

# Create your models here.
class Employee(models.Model):
    uid = models.IntegerField()
    empname = models.CharField(max_length=64)
    pic = models.CharField(max_length=64)
    sex = models.CharField(max_length=63, null=True)
    birth = models.CharField(max_length=63, null=True)
    img = models.CharField(max_length=63, null=True)
    nation = models.CharField(max_length=63, null=True)
    empstatus = models.CharField(max_length=63, null=True)
    edu = models.CharField(max_length=63, null=True)
    address = models.CharField(max_length=10, null=True)
    merr = models.CharField(max_length=63, null=True)
    idcard = models.CharField(max_length=63, null=True)
    phone = models.CharField(max_length=63, null=True)
    idAddress = models.CharField(max_length=63, null=True)
    idwork = models.CharField(max_length=63, null=True)
    datework = models.CharField(max_length=63, null=True)
    postwork = models.CharField(max_length=63, null=True)
    levelwork = models.CharField(max_length=63, null=True)
    topworkid = models.IntegerField()
    depid = models.IntegerField()
    statuswork = models.CharField(max_length=63, null=True)

    def __str__(self):
        return self._get_pk_val

    class Meta:
        db_table = "employee"
