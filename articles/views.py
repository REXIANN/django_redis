from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    contest = {
        'articles': articles
    }
    return render(request, 'articles/index.html')
