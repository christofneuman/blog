from django.shortcuts import render
from django.views import generic

from blog.models import Blog


def home(request):
    return render(request, "home.html", {})


def resources(request):
    return render(request, "resources.html", {})


def blog(request):
    posts = Blog.objects.published()

    return render(request, "blog.html", {
        'posts': posts
    })


class BlogIndex(generic.ListView):
    queryset = Blog.objects.published()
    template_name = "blog.html"
    paginate_by = 3


class BlogDetail(generic.DetailView):
    model = Blog
    template_name = "post.html"
