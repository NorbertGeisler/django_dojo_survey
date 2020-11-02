from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def result(request):
    context={
        'form_name': request.POST['form_name'],
        'dojo_location': request.POST['dojo_location'],
        'favorite_language': request.POST['favorite_language'],
        'form_comment': request.POST['form_comment'],
    }
    return render(request, 'result.html', context)
# Create your views here.
