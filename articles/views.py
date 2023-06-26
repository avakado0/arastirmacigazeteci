from django.shortcuts import redirect, render, get_object_or_404
from .models import Article
from .forms import ArticleCreationForm

def starting_page(request):
    return redirect('article_list')

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/article_detail.html', {'article': article})

def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:article_list')
    else:
        form = ArticleForm()
    
    context = {'form': form}
    return render(request, 'articles/article_create.html', context)
