from django.shortcuts import render
from django.http import HttpResponse
from bs_scrap import scrap
from dataconverter import convert
from rf_model import rf_model

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

      userdata, profile_img = scrap(username)

      username = userdata['username']
      pname = userdata['profilename']
      flwrs = userdata['followers']  
      flwing = userdata['following']
      posts = userdata['posts']
      bio = userdata['bio']
      ppic = userdata['profilepic']
      extlink = userdata['extlink']
      accstat = userdata['privateaccount']


      converteddata = convert(userdata)
      prediction = rf_model(converteddata)

      if prediction[0] == 0:
         prediction ="n"
      else:
         prediction = "y" 
      if accstat == 1:
         accstat ="Yes"
      else:
         accstat = "No"
      if ppic == 1:
         ppic ="Yes"
      else:
         ppic = "No"
      if extlink == 1:
         extlink ="Yes"
      else:
         extlink = "No"
   
      context = {'username': username, 'pname':pname, 'flwrs':flwrs, 'flwing':flwing, 'posts':posts, 
                 'bio':bio, 'ppic':ppic, 'extlink':extlink, 'accstat':accstat, 'profile_img':profile_img, 
                 'dataset':converteddata, 'prediction':prediction }
      
   return render(request, 'ffmain/index.html', context)