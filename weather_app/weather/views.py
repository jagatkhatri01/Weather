from django.shortcuts import render

# Create your views here.

def home(request):
    if request.method == "POST":
        city = request.POST.get('city')

    else:
        city = ''
    
    return render(request, "index.html", {'city':city})
