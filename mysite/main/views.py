from django.shortcuts import render, redirect
from .models import HomeLogo, HomeBgInfo, HomeSlider, Lastest_Episode
from .forms import EpisodeForm
# Create your views here.

def global_items():
    home_logo = HomeLogo.objects.all()[0]
    return home_logo

def index(request):
    button = request.POST.get('button')
    button = int(button)
        # if form.is_valid():
            # Lastest_Episode.objects.update(**form.changed_data)
    home_bg_info = HomeBgInfo.objects.all()
    home_slider = HomeSlider.objects.all()
    episodes = Lastest_Episode.objects.all()
    return render(request, 'main/index.html', context={
    'nbar': 'home',
    'home_logo': global_items(),
    'home_bg_info':home_bg_info,
    'home_slider':home_slider,
    'episodes':episodes,
    })

def detail_page(request):
    return render(request, 'main/detail-page.html', context={
    'nbar': 'detail_page',
    'home_logo': global_items()

        
    })

def listing_page(request):
    return render(request, 'main/listing-page.html', context={
    'nbar': 'listing_page',
    'home_logo': global_items()
        
    })

def contact(request):
    return render(request, 'main/contact.html', context={
    'nbar': 'contact',
    'home_logo': global_items()

        
    })

def about(request):
    return render(request, 'main/about.html', context={
    'nbar': 'about',
    'home_logo': global_items()
        
    })