from django.shortcuts import render

def index(request):
    template = 'blog/index.html'
    return render(request, template)


def post_detail(request, pk):
    template = 'detail/html'
    context = 
    return render(request, template, context)


def category_posts(request, pk):
    template = 'category.html'
    context = 
    return render(request, template, context)