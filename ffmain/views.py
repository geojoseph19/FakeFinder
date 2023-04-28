from django.shortcuts import render
from django.http import HttpResponse
from bs_scrap import scrap
from dataconverter import convert

# Create your views here.
def home(request):
   # return HttpResponse("Yepp")
   cc = "asadsaff"
   context = {'optext': cc}
   return render(request, "ffmain/index.html",context)

def testing(request):
   if request.method == 'POST':
      prof_link = request.POST.get('input')
      if prof_link[0:26] == "https://www.instagram.com/":
         username = prof_link[26:-1]
      else:
         username = prof_link

      userdata = scrap(username)
      converteddata = convert(userdata)
      context = {'userdata': userdata, 'dataset':converteddata}
      
   return render(request, 'ffmain/index.html', context)