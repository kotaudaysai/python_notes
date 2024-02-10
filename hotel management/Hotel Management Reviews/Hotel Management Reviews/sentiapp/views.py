from django.shortcuts import render
from django.views.generic import TemplateView
import json
from  .models import user
# Importing the libraries

import pandas as pd

import pickle

clf = pickle.load(open("algo.pk", "rb"))
cv1 = pickle.load(open("tranform.pkl", "rb"))



def  fake(request):

    return render(request,'fake.html')

def  normal(request):
    return render(request,'normal.html')
#################### RF#######################
def review(request):
    return render(request,'review.html')
########################################################################    
def clas(request):

    if request.method == 'POST':
          name = request.POST.get('num1')
          hotel = request.POST.get("num2")
          email = request.POST.get('email')
          text = request.POST.get('text')

          data = [text]
          
          vect = cv1.transform(data).toarray()
         
          if clf.predict(vect) == [0]:
               my = "Fake"
               reg = user(name=name,email=email ,hotel=hotel,review=text,result=my)
               reg.save()

          else:
               my = "Truthfull"
               reg = user(name=name,email=email ,hotel=hotel,review=text,result=my)
               reg.save()

          print(my)
          context = {"result":my}
          return render(request,'normal.html',context)
    else:
        return render(request, 'clas.html')


class home(TemplateView):
    template_name = 'home.html'