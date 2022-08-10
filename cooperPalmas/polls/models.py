import datetime
from django.db import models
from django.utils import timezone   


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    
class Category(models.Model):
    slug = models.CharField(max_length=20,primary_key=True)         

    
class Author(models.Model):
    photo = models.FileField(upload_to='cooperPalmas/polls/img/perfil')
    name = models.CharField(max_length=50, primary_key=True)
    bio = models.CharField(max_length=100)
    
        

class Post(models.Model):
    created_at = models.DateTimeField()
    title = models.CharField(max_length=250)    
    excerpt = models.TextField()
    featured_image = models.FileField(upload_to='cooperPalmas/polls/img')  
    slug = models.ForeignKey(Category, on_delete=models.CASCADE)
    autor = models.ForeignKey(Author,on_delete=models.CASCADE)  
    
    