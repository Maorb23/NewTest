from django.urls import path

from . import views



from django.urls import path

from . import views

app_name = 'Maor_proj.polls'

urlpatterns = [
    #path('', views.main_index, name='main_index'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
