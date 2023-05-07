from django.shortcuts import render
from django.http import HttpResponse
from bs_scrap import scrap
from dataconverter import convert
from rf_model import rf_model
from lstm_model import lstm_model
from knn_model import knn_model
import json

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
         userdata, profile_img = scrap(username)
         
      elif len(prof_link) < 4:
         return render(request, "ffmain/index.html")
      
      elif prof_link[0] == '[':
         strdata = json.loads(prof_link)
         x = strdata
         #x =["pub", "geojoseph19" , "51 posts 2,596 followers 925 following","Geo Joseph",["Unveiling Soon🌀"], 1,1]

         if x[0] == "pub":
            accstat = 0
         else:
            accstat = 1
         username = x[1]
         y = x[2]
         posts = y[0:y.find('posts')]
         posts = str(posts).replace(",","")

         flwrs = y[y.find('posts')+6:y.find('followers')-1]
         flwrs = str(flwrs).replace(",","")

         flwing = y[y.find('followers')+10:y.find('following')-1]
         flwing = str(flwing).replace(",","")
          
         #converting number abbrevations 
         flwrs = str(flwrs)
         if flwrs[-1] == "M":
               flwrs = flwrs[0:-1] 
               print(flwrs)
               flwrs = int(flwrs) * 1000000
         elif flwrs[-1] == "K":
               flwrs = flwrs[0:-1] 
               flwrs = int(flwrs) * 1000


         posts = str(posts)
         if posts[-1] == "M":
               posts = posts[0:-1] 
               print(posts)
               posts = int(posts) * 1000000
         elif posts[-1] == "K":
               posts = posts[0:-1] 
               posts = int(posts) * 1000

         pname = x[3]
         bio = x[4][0]
         ppic = x[5]
         extlink = x[6]

         userdata = {'username':username, 'profilename':pname, 'followers':flwrs,
                     'following':flwing, 'posts':posts, 'bio':bio, 'profilepic':ppic, 
                     'extlink':extlink, 'privateaccount':accstat}
         profile_img = "null"


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
      rf_pred = rf_model(converteddata)
      lstm_pred = lstm_model(converteddata)
      knn_pred = knn_model(converteddata)

      #------Finding average-------
      x = rf_pred[0]
      y = lstm_pred[0]
      z = knn_pred[0]
      # Convert binary to decimal
      x_dec = int(str(x), 2)
      y_dec = int(str(y), 2)
      z_dec = int(str(z), 2)

      # Find average of decimal values
      avg_dec = int(round((x_dec + y_dec + z_dec) / 3))

      # Convert decimal average to binary
      avg_bin = bin(avg_dec)[2:]

      # Pad with leading zeros if necessary
      prediction = avg_bin.zfill(1)
      prediction = int(prediction)

      if prediction == 0:
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
                 'dataset':converteddata, 'prediction':prediction, 'lstmpred':lstm_pred, 'knnpred' : knn_pred }
      
   return render(request, 'ffmain/index.html', context)


def manual(request):

   if request.method == 'POST':
      context = request.POST.get('input')


   

   return render(request, 'ffmain/index.html', context)