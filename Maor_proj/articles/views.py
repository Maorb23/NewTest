#from django.shortcuts import render
#from django.shortcuts import get_object_or_404
"""
def article_view(request):
    return render(request, 'articles/article_home.html')

def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'articles/article_detail.html', {'article': article})
"""


"""
from django.shortcuts import render, get_object_or_404
from .models import Article  # Ensure you have an Article model

def article_view(request):
    article_id = request.GET.get('article_id')
    
    if article_id:
        # Fetch the selected article
        selected_article = get_object_or_404(Article, id=article_id)
        # Exclude the selected article from the list of other articles
        other_articles = Article.objects.exclude(id=article_id)
    else:
        # If no article is selected, you can choose to display a default article or none
        selected_article = None
        other_articles = Article.objects.all()
    
    context = {
        'selected_article': selected_article,
        'other_articles': other_articles,
    }
    
    return render(request, 'articles/article_template.html', context)
"""
# articles/views.py
import os
from django.conf import settings
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

def list_articles(request):
    
    articles_dir = os.path.join(settings.MEDIA_ROOT, 'articles')
    try:
        # List all files in the articles directory
        all_files = os.listdir(articles_dir)
        # Filter only PDF files (or other types as needed)
        articles = [f for f in all_files if f.lower().endswith('.pdf')]
    except FileNotFoundError:
        articles = []

    # Get selected article from GET parameters
    selected_article = request.GET.get('article')

    if selected_article:
        if selected_article not in articles:
            raise Http404("Article does not exist.")
        # Exclude the selected article from the list of other articles
        other_articles = [f for f in articles if f != selected_article]
    else:
        selected_article = None
        other_articles = articles

    context = {
        'selected_article': selected_article,
        'other_articles': other_articles,
    }

    return render(request, 'articles/article_template.html', context)

