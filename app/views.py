from django.shortcuts import render

def jinja_print(request):
    d ={'name':'RANJITHA Adhikari','age':23}
    return render(request,'jinja_print.html',context=d)
