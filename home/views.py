from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homePage(request):
    params = {
        'title':'http://bridge-tohoku.com/',
        'msg':'このページはホームです',
    }
    return render(request, 'home/home.html', params)

# def articlePage(request, article):
#     params = {
#         'title':'http://bridge-tohoku.com/report',
#         'msg':'これはサンプルで作ったページです',
#         'goto':'indexPage',
#         'article':article,
#     }
#     return render(request, 'home/article.html', params)


