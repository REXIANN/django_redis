from django.shortcuts import render
from articles.models import Article
from django.core.cache import cache
import json

DEFAULT_TIMEOUT = 25

def index(request):
    articles = cache.get("articles")
    if not articles:
        articles = Article.objects.order_by('-pk')
        jsonString = json.dumps(articles)
        cache.set("articles", jsonString, timeout=DEFAULT_TIMEOUT)
    else:
        jsonString = cache.get("articles")
        articles = json.loads(jsonString)
    
    context = { 'articles': articles }
    return render(request, 'index.html', context)
