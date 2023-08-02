from django.shortcuts import render
from django.http import HttpResponse
from .models import anime_list
from animego import animegoParse

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

def add_data_to_list(request):
    new_year = request.GET.get('new_year')
    new_season = request.GET.get('new_season')
    print(new_season, new_year)
    if new_season and new_year:
        parser = animegoParse(season= new_season, year=new_year)
        anime_lst = anime_list.objects.filter(year=new_year, season=new_season)
    else:
        anime_lst = anime_list.objects.all()
    return render(request, 'main/anime_list.html', {'anime_lst': anime_lst})
