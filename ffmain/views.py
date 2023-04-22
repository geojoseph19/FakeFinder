from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
   # return HttpResponse("Yepp")
   return render(request, "ffmain/index.html")