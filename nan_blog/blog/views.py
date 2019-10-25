from django.shortcuts import render

# Create your views here.
def home(request):
    
    data={}
    return render(request, 'pages/blog/index.html',data)

def detail(request):
    
    data={}
    return render(request, 'pages/blog/blog-detail.html',data)

def category(request):
    
    data={}
    return render(request, 'pages/blog/category.html',data)

def archive(request):
    
    data={}
    return render(request, 'pages/blog/archive.html',data)

def element(request):
    
    data={}
    return render(request, 'pages/blog/element.html',data)