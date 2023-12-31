from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

# Create your views here.


def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)

    return render(request, "core/frontpage.html", {"posts": posts})


def about(request):
    return render(request, "core/about.html")


def robots_txt(request):
    text = [
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /search/",
        "Disallow: /category/",
        "Disallow: /comment/",

    ]
    return HttpResponse("\n".join(text), content_type="text/plain")
