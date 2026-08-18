from django.shortcuts import render
from django.http import JsonResponse
import random
import json

# ========== الصفحة الرئيسية ==========
def home(request):
    return render(request, 'home.html')

# ========== لعبة Snake ==========
def snake(request):
    return render(request, 'snake.html')

# ========== لعبة Wordle (تخمين الكلمات) ==========
def wordle(request):
    return render(request, 'wordle.html')

# API لجلب كلمة عشوائية
def get_word(request):
    words = ['python', 'django', 'game', 'code', 'brain', 'react', 'vscode']
    return JsonResponse({'word': random.choice(words)})

# ========== لعبة Dots & Boxes ==========
def dots_boxes(request):
    return render(request, 'dots_boxes.html')