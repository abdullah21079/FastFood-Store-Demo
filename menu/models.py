from django.db import models

# Create your models here.
class Menu(models.Model):
    name=models.CharField(max_length=20)
    description= models.CharField(max_length=500)
    price=models.IntegerField()
    image=models.ImageField(upload_to="Menu")


    def __str__(self):
        return self.name