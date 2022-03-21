from django.contrib import admin

# Register your models here.
from .models import ComputerBrands
from .models import ComputerSpecification
from .models import Computer


class AdminComputerBrands(admin.ModelAdmin):
    list_display = ['brandname', 'logo']


admin.site.register(ComputerBrands, AdminComputerBrands)


class AdminComputerSpecification(admin.ModelAdmin):
    list_display = ['generation', 'price_min', 'price_max', 'ram', 'brandname']


admin.site.register(ComputerSpecification, AdminComputerSpecification)

admin.site.register(Computer)