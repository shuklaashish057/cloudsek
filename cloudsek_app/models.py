from django.db import models

# Create your models here.
class Amount(models.Model):
    id_pk= models.CharField(max_length=300, unique=True)
    number_1 = models.IntegerField()
    number_2 = models.IntegerField()
    total = models.IntegerField()
    
    def __str__(self):

        return  self.id_pk