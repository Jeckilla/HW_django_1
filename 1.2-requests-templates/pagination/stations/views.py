from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open('data-398-2018-08-30.csv', 'r', encoding='utf-8') as f:
        content = csv.DictReader(f)
        bs_list = []
        for station in content:
            bs_list.append(station)

    per_page = 10
    paginator = Paginator(bs_list, per_page)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    bus_stations = page.object_list
    context = {
        'bus_stations': bus_stations,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
