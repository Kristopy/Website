from django.views.generic import TemplateView
from django.shortcuts import render


# Create your views here.

"""
This is not class-based views
from django.http import HttpResponse
from django.shortcuts import render

def HomePageView(request):
    return(HttpResponse("Hello world"))
"""

class HomePageView(TemplateView):
    template_name = 'Home.html'

class PhononsPageView(TemplateView):
    template_name = 'Phonons.html'

class ElectronsPageView(TemplateView):
    template_name = 'Electrons.html'

def HeatCapacityPage(request):
    return render(request, 'HeatCapacity.html')

def Phonons_EnergyPage(request):
    return render(request, 'Phonons_Energy.html')

def Phonons_1D_chainPage(request):
    return render(request, 'Phonons_1D_chain.html')

"""
def buttonpages(request):

    def Button_function(i):
        a = "{{%\n static \"Phonons_{}.mp4\" %\n}}".format(i)
        document.getElementById("demo").src = a
        return a

    return render(request,'Phonons', {"Button_function(i)":Button_function})
"""
