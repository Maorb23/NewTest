from django.urls import path
from . import views

app_name = 'Maor_proj.articles'
"""
urlpatterns = [
    path('', views.article_view, name='article_home'),
    path('<int:id>/', views.article_detail, name='article_detail'),
    # Add more CV-related URLs if needed
]
"""

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_articles, name='list_articles'),
    path('view/<str:article_name>/', views.view_article, name='view_article'),
]
