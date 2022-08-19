from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('', views.land_page, name='landPage'),
    path('contato/', views.contato, name='contato'),
    path('regimentos/', views.contato, name='regimentos'),
    path('blog/', views.PostList.as_view(), name='home'),
    path('recent/', views.testAA, name='recents'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.category, name='category_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)