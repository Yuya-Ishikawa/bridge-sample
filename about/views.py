from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def aboutPage(request):
    params = {
        'title':'http://bridge-tohoku.com/about',
        'msg':'これはサンプルで作ったページです',
    }
    return render(request, 'about/about.html', params)

def articlePage(request, article):
    params = {
        'title':'http://bridge-tohoku.com/about',
        'msg':'これは記事ページです',
        'article':article,
    }
    return render(request, 'about/article.html', params)


