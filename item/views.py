from django.http import HttpResponse


def post(request, post_id):
    return HttpResponse('post_id は = {} です'.format(post_id))


def news(request, slug):
    return HttpResponse('slug は = {} です'.format(slug))


# Create your views here.
