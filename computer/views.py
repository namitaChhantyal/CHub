from pyexpat import model
from urllib import request
from django.http import HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect, reverse
from .models import ComputerBrands
from .models import ComputerSpecification
from .models import Computer
from django.views.generic import ListView, CreateView, UpdateView, DetailView,TemplateView
from django.contrib import messages
from .forms import ComputerForm


class IndexView(ListView):
    model = ComputerBrands
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        queryset = ComputerBrands.get_all_computerbrands()
        context = {
            'brands': queryset
        }
        return context


class ComputerDetailsView(ListView):
    model = Computer
    template_name = 'details.html'

    def get_queryset(self):
        queryset = Computer.objects.all()
        return queryset

# class IndexView(ListView):
#     def get(self, request, *args, **kwargs):
#         prds = ComputerBrands.get_all_computerbrands()
#     # print(products)
#         return render(request, 'index.html', {'brands': prds})

# class DetailsView(ListView):
#     def get(self,request,*args,**kwargs):
#          ds=ComputerSpecification.get_all_computerspecifications()
#          return render(request,'details.html',{'specdetails':ds})

# def index(request):
#     prds = ComputerBrands.get_all_computerbrands()
#     # print(products)
#     return render(request, 'index.html', {'brands': prds})

# def details(request):
#     ds=ComputerSpecification.get_all_computerspecifications()
#     return render(request,'details.html',{'specdetails':ds})


class FormView(CreateView):
    model = Computer
    template_name = 'form.html'
    form_class = ComputerForm

    def post(self, request):
        form = ComputerForm(request.POST)
        unitprice = int(request.POST.get('unitrate'))
        quantity = int(request.POST.get('quantity'))
        form.instance.totalprice = unitprice*quantity

        if form.is_valid():
            form.save()
            return redirect("/")
        return render(request, 'index.html')

    # if the form is valid,redirect to the supplied url
    # def form_valid(self, form):
    #     unitprice = form.cleaned_data.get('unitrate')
    #     quantity = form.cleaned_data.get('quantity')
    #     form.instance.totalprice = unitprice*quantity
    #     return super(FormView, self).form_valid(form)

    def get_success_url(self):
        return reverse("index")


class UpdateViewForm(UpdateView):
    template_name = 'update.html'
    form_class = ComputerForm

    def get_queryset(self):
        queryset = Computer.objects.all()
        return queryset

    def get_success_url(self):
        return reverse("index")


class IndividualDetailView(DetailView):
    model = Computer
    template_name = 'individualdetail.html'

    def get_queryset(self):
        queryset = Computer.objects.all()
        return queryset

class LogoDetailView(ListView):
    model=Computer
    template_name = "logodetail.html"

    def get_queryset(self):
        val = self.kwargs.get("brandname")
        brand = Computer.objects.filter(brandname__icontains=val)   
        return brand
       

    
        
        

# def form(request):
#     if request.method == 'POST':
#         postDate = request.POST
#         computercode=postDate.get('computercode')
#         brandname = postDate.get('brandname')
#         quantity = postDate.get('quantity')
#         unitrate = postDate.get('unitrate')
#         totalprice=postDate.get('totalprice')

#         order_info = Computer(computercode=computercode,brandname=brandname,
#                            quantity=quantity,
#                            unitrate=unitrate, totalprice=totalprice)
#         order_info.register()

#         messages.info(request,"successfully ordered.")

#     else:
#         return render(request, 'form.html')
