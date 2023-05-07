from django.shortcuts import render

# Create your views here.

def index(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = request.META.get('REMOTE_ADDR')
    print(ip)
    print(x_forwarded_for)
    return render(request, 'index.html')