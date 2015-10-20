from django.shortcuts import render, redirect
from django.views import generic

from blog.models import Blog

from blog.forms import ContactMeForm


def home(request):
    form = ContactMeForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('thanks')

    return render(request, "home.html", {
        'form': form
    })


def thanks(request):
    return render(request, 'thanks.html', {})


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
