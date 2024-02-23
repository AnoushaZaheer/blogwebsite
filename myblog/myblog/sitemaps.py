from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from core.models import Category, post

class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()

class PostSitemap(Sitemap):
    def items(self):
        return post.objects.filter(status=post.ACTIVE)
    
    def lastmod(self, obj):
        return obj.created_at