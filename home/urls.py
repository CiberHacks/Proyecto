from django.urls import path

from home import views

app_name = "home"

urlpatterns = [
    path('',views.index.as_view(), name='index')


    
]