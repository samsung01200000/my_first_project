from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Player, GameScore
import random
import json

def home(request):
    return render(request, 'games/home.html')

def snake(request):
    return render(request, 'games/snake.html')

def wordle(request):
    return render(request, 'games/wordle.html')

def dots_boxes(request):
    return render(request, 'games/dots_boxes.html')

def get_word(request):
    words = ['python', 'django', 'game', 'code', 'brain', 'react', 'vscode']
    return JsonResponse({'word': random.choice(words)})

@csrf_exempt
def save_score(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        player_name = data.get('player_name')
        game = data.get('game')
        score = data.get('score')
        player, created = Player.objects.get_or_create(name=player_name)
        GameScore.objects.create(player=player, game=game, score=score)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

def leaderboard(request):
    games = ['snake', 'wordle', 'dots']
    leaderboard_data = {}
    for game in games:
        top_scores = GameScore.objects.filter(game=game).order_by('-score')[:5]
        leaderboard_data[game] = [
            {'player': score.player.name, 'score': score.score}
            for score in top_scores
        ]
    return render(request, 'games/leaderboard.html', {'leaderboard': leaderboard_data})