from django.db import models

class Disease(models.Model):
    Did = models.IntegerField()
    Dname = models.CharField(max_length=25)
    prec = models.CharField(max_length=25)
    class Meta:
        db_table = 'Disease'
