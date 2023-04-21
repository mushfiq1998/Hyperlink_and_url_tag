from django.shortcuts import render

# Create your views here.
'''
def learn_django(request):
    return render(request, 'course/courseinfo.html')
'''

# Second approach to use hyperlink
def learn_django(request):
    return render(request, 'course/courseinfo.html',
                   {'learn_dj': '/cor/learndj'})
