from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
import json
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import userdb

# Create your views here.


def index(request):
    print('come in1')
    print(request.method)
    if request.method == "POST":
        print('come in 2')
        print(request.POST.get('name',''))
        newname =request.POST.get('name', '')
        newage=request.POST.get('age', '')
        newskill=request.POST.get('skills','')
        if (newname!=""):
            obj1 = userdb.objects.get(id=1)
            obj1.user_name = newname
            obj1.age = newage
            obj1.skills = newskill
            obj1.save()
        return HttpResponse()
    user1 = userdb.objects.all()
    print(user1[0])
    params = {
        'username' : user1[0].user_name,
        'userage' : user1[0].age,
        'userskills' : user1[0].skills,
        'userpic1' : user1[0].image1,
        'userpic2' : user1[0].image2
    }
    print(params['username'])
    return render(request,'userprof/index.html',{'params':params})