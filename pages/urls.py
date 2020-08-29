from django.urls import path
#from .views import HomePageView
from django.conf import settings
from .views import HomePageView, PhononsPageView, ElectronsPageView,Phonons_1D_chainPage, Phonons_EnergyPage, HeatCapacityPage
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePageView.as_view() ,name='Home'),
    path('Phonons/', PhononsPageView.as_view(), name='Phonons'),
    path('Electrons/', ElectronsPageView.as_view(), name='Electrons'),
    path('Scripts/Phonons_1D_chain.py/', Phonons_1D_chainPage, name='Phonons_1D_chain'),
    path('Scripts/Phonons_Energy.py/', Phonons_EnergyPage, name='Phonons_Energy'),
    path('Scripts/HeatCapacity.py/', HeatCapacityPage, name='HeatCapacity'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
