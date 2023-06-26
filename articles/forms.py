from django import forms
from .models import Article
from django import forms
from .models import Article

class ArticleCreationForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'slug', 'author', 'publication_date', 'content']
