from django.shortcuts import render
from django.http import HttpResponse
from bs_scrap import scrap
from dataconverter import convert
from rf_model import rf_model
from lstm_model import lstm_model
from knn_model import knn_model

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

      if prediction == 0:
         prediction ="n"
      else:
         rf_pred = "y" 
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