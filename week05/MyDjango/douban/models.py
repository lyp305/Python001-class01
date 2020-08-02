from django.db import models


# Create your models here.
class Comments(models.Model):
    id = models.BigAutoField(primary_key=True)
    mrank = models.IntegerField()
    mcomments = models.CharField(max_length=1000)
    metime = models.CharField(max_length=32)

    class Meta:
        db_table = 'comments'
