import requests
from django.contrib.auth.models import User
from django.http import response, HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup, NavigableString


from .models import Newsarticle


def index(request):
    url="https://techcrunch.com/"
    req = requests.get(url).text
    soup=BeautifulSoup(req,'lxml')
    for article in soup.find_all('div', class_='post-block post-block--image post-block--unread'):
        title1 = article.header.h2.a.text
        title=title1.strip()
        author1 = article.header.find('span', class_='river-byline__authors').text
        author=author1.strip()
        timestamp=article.header.time['datetime']
        img=article.footer.a.img['src']


        Newsarticle1 = Newsarticle.objects.create(timestamp=timestamp,news_title=title,img_source_url=img,author=author)


        Newsarticle1.save();

    return render(request, 'index.html')

def home(request):
    info=Newsarticle.objects.filter().order_by('id')[:20]

    return render(request,"home.html", {'info': info})