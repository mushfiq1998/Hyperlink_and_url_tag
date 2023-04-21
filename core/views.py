from django.shortcuts import render

# Create your views here.
'''
# First approach to use hyperlink:
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')
'''

# Second approach to use hyperlink:
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html', {'abc': '/about'})

'''
# Third approach to use hyperlink:
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')
'''