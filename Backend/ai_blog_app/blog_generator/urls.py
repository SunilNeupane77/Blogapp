from django.urls import path
from . import views
urlpatterns = [
    # all of the urls in the 
    path("",views.index, name='index')
]
