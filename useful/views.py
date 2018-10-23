from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def usefulPage(request):
    params = {
        'title':'http://bridge-tohoku.com/useful',
        'msg':'これはサンプルで作ったページです',
    }
    return render(request, 'useful/useful.html', params)

def articlePage(request, article):
    params = {
        'title':'http://bridge-tohoku.com/useful',
        'msg':'これはサンプルで作ったページです',
        'article':article,
    }
    return render(request, 'useful/article.html', params)


