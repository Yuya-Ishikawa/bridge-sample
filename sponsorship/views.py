from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sponsorshipPage(request):
    params = {
        'title':'http://bridge-tohoku.com/sponsorship',
        'msg':'これはサンプルで作ったページです',
    }
    return render(request, 'sponsorship/sponsorship.html', params)

def articlePage(request, article):
    params = {
        'title':'http://bridge-tohoku.com/report',
        'msg':'これはサンプルで作ったページです',
        'article':article,
    }
    return render(request, 'report/article.html', params)


