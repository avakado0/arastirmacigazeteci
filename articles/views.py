from django.shortcuts import redirect, render, get_object_or_404
from .models import Article

def starting_page(request):
    return redirect('article_list')

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/article_detail.html', {'article': article})
