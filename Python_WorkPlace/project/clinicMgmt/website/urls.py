from django.contrib import admin
from django.urls import path,include
from website import views
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    path('',views.web_index,name='index'),
    path('consultation',views.web_consultation,name='consultation'),
    path('diagnostic',views.web_diagnostic,name='diagnostic'),
    path('pharmacy',views.web_pharmacy,name='pharmacy'), 
    path('covid19',views.web_covid19,name='covid19'),
                     
]
