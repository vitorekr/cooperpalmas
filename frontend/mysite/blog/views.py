from django.views import generic
from .models import Post, Category
from django.shortcuts import get_object_or_404, redirect, render

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

# def postDetail(request):
#     detail_list = Post.objects.filter(status=1).order_by('-created_on')
#     context = {'detail_list': detail_list}
#     return render(request, 'post_detail.html', context)

def contato(request):
    return render(request, 'teste.html')

def land_page(request):
    return render(request, 'teste.html')

def regimentos(request):
    return render(request, 'teste.html')

def testAA(request):
    test_list = Post.objects.order_by('-created_on')[:3]
    context = {'test_list': test_list}
    return render(request, 'post_detail.html', context)



def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)

    return render(request, 'blog/category.html', {'category': category, 'posts': posts})