from django.views import generic
from .models import Post, Category
from django.shortcuts import get_object_or_404, redirect, render

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')   
    template_name = 'blogTest.html'

class PostIndex(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')   
    template_name = 'landing.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

# def postDetail(request):
#     detail_list = Post.objects.filter(status=1).order_by('-created_on')
#     context = {'detail_list': detail_list}
#     return render(request, 'post_detail.html', context)
'''
def landing(request):
    return render(request, 'landing.html')'''
   

def sobre(request):
    return render(request, 'sobre.html')

def land_page(request):
    return render(request, 'index.html')

def regimentos(request):
    return render(request, 'regimentos.html')

def estatuto(request):
    return render(request, 'estatuto.html')

def contato(request):
    return render (request, 'contact.html')

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)    
    return render(request, 'blog/category.html', {'category': category, 'posts': posts})