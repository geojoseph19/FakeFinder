from django.shortcuts import render
from django.http import HttpResponse
#from sample import tests

# Create your views here.
def home(request):
   # return HttpResponse("Yepp")
   cc = "asadsaff"
   context = {'optext': cc}
   return render(request, "ffmain/index.html",context)

def testing(request):
   if request.method == 'POST':
      cc = request.POST.get('input')
      context = {'optext': cc}
   return render(request, 'ffmain/index.html', context)