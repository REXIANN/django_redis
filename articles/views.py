from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm
# Create your views here.
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = { 'article': article }
    return render(request, 'articles/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('/')
    else:
        form = ArticleForm()
    
    context = { 'form': form }
    return render(request, 'articles/form.html', context)