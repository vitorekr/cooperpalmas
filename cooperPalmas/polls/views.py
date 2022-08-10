from django.http import HttpResponse
from django_nextjs.render import render_nextjs_page_sync

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


#