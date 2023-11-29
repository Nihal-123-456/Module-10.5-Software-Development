from django.shortcuts import render
import datetime
# Create your views here.
def apphome(request):
    info = {'age':18, 'quo':"i'm in", 'date':datetime.datetime.now(),
            'list': [{'name': 'zed', 'age': 19}, {'name': 'amy', 'age': 22}, {'name': 'joe', 'age': 31},],
            'arr':['a','b','v'],'line':'''i
            am
            legend''','text':'I am Legend','s_date': datetime.datetime(2021,5,10),
            'e_date':datetime.datetime(2022,6,11)}
    return render(request,'app_1/apphome.html',info)