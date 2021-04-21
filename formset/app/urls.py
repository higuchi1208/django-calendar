from django.urls import path 
from . import views 

urlpatterns = [
  path('', views.make_test_modelformset, name="formset"),
  
]