from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.PostIndex.as_view(), name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('regimentos/', views.regimentos, name='regimentos'),
    path('estatuto/', views.estatuto, name='estatuto'),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('recent/', views.testAA, name='recents'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.category, name='category_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)