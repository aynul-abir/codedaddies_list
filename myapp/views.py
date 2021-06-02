import requests
from urllib.parse import quote_plus
from django.shortcuts import render
from bs4 import BeautifulSoup
from . import models


BASE_CRAIGSLIST_URL = 'https://www.daraz.com.bd/catalog/?q={}'


# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    print(final_url)
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')

    post_titles = soup.find_all('div', {'class': 'c5TXIP'})
    print(post_titles)
    #print(data)
    stuff_for_frontend = {
        'search': search,
    }
    return render(request, 'myapp/new_search.html', stuff_for_frontend)
