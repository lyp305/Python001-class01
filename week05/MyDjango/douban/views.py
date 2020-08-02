from django.shortcuts import render

from .models import Comments

# Create your views here.
def comments(request):
    ###  从models取数据传给template  ###
    filterc ={'mrank__gte': 30}
    comments = Comments.objects.filter(**filterc)

    data={
        'data':comments
    }

    # return render(request, 'douban.html', locals())
    return render(request, 'comments.html', data)