from django.shortcuts import render
from django.http import HttpResponse
from .models import anime_list

def index(request):
    return render(request, "main/index.html")

def get_anime_season(request):
    return render(request, "main/anime_list_form.html")

def get_anime_list(request):
    selected_year = request.GET.get('year')
    selected_season = request.GET.get('season')
    print(selected_year, selected_season)
    if selected_year and selected_season:
        anime_lst = anime_list.objects.filter(year=selected_year, season=selected_season)
    else:
        # If no year and season selected, show all Anime objects
        anime_lst = anime_list.objects.all()
    return render(request, 'main/anime_list.html', {'anime_lst': anime_lst})