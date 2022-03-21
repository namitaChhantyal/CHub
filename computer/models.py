from django.db import models

# Create your models here.


class ComputerBrands(models.Model):
    brandname = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='uploads/products/')

    
    @staticmethod
    def get_all_computerbrands(): #it returns all objects and this method is used in views.py
        return ComputerBrands.objects.all()

    def __str__(self):
        return self.brandname


class ComputerSpecification(models.Model):
    generation = models.CharField(max_length=50)
    price_min = models.IntegerField(default=0)
    price_max = models.IntegerField(default=0)
    ram = models.IntegerField(default=0)
    brandname = models.ForeignKey(ComputerBrands, on_delete=models.CASCADE)

    def __str__(self): #it displays the name instead of showing computerspecification object(1) and so on
        return self.generation

    # @staticmethod
    # def get_all_computerspecifications():
    #     return ComputerSpecification.objects.all()

class Computer(models.Model):
    computercode=models.IntegerField(unique=True)
    brandname = models.CharField(max_length=50, null=True, blank=True)
    # QUANTITY_CHOICES = (
    #     ('1', '1'),
    #     ('2', '2'),
    #     ('3', '3'),
    #     ('4', '4'),
    #     ('5', '5'),
    # )
    quantity = models.IntegerField()
    computer=models.ForeignKey(ComputerSpecification,on_delete=models.CASCADE)
    unitrate = models.IntegerField()
    totalprice = models.IntegerField()

    def register(self):
        self.save()
    
   
