"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
# from . import views
from blog.views import home,about
from core.views import details,category,search, robots_txt
from django.contrib.sitemaps.views import sitemap
from .sitemaps import CategorySitemap, PostSitemap
sitemaps = {'category': CategorySitemap, 'post': PostSitemap}
urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('about/', about, name='about'),
    path('search/', search, name='search'),
    # path('<slug:slug>/',details,name='details')
    path('<slug:category_slug>/<slug:slug>/', details, name='details'),
    path('<slug:slug>/', category, name='category_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
