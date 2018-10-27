from django.shortcuts import render

# Create your views here.

index_dict = {'text': 'hello world!',
              'number': 100}

def index(request):
    return render(request, 'basic_app/index.html', context=index_dict)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')
