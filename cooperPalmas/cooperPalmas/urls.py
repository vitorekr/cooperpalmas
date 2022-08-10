from django.contrib import admin
from django.urls import include, path
from .views import index
from . import views

urlpatterns = [
   # path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),   
    path('', views.index, name='index'),
   # path("index/", index, name="index"),
]