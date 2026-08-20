from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('snake/', views.snake, name='snake'),
    path('wordle/', views.wordle, name='wordle'),
    path('dots-boxes/', views.dots_boxes, name='dots_boxes'),
    path('get-word/', views.get_word, name='get_word'),
    path('save-score/', views.save_score, name='save_score'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]