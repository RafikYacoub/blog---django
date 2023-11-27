from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from blog.models import Post, Category


class CategortSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Category.objects.all()


class PostSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.objects.filter(status=Post.ACTIVE)

    def lastmod(self, obj):
        return obj.date
