from django.contrib import admin

from .models import Author, Question, Category, Post

# Site Administration (Campos dos Posts, etc)

admin.site.register(Question)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Category)