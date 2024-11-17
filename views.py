from django.shortcuts import render

def home_views(request):
    return render(request, 'gvk_site/home_page.html')




