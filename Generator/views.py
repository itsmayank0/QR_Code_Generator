from django.shortcuts import render
from qrcode import *
from .models import *
image_name =None

def HomeView(request):
    all_data = equipments.objects.all()
    return render(request, "Home.html", {'equipments': all_data})

def generate_qr(request):
    if request.method=='GET':
        S=request.GET["station_data"]
        E=request.GET["equipment"]
        T=request.GET['type']
        M=request.GET["model_number"]
        image_name = E+M+T
        data_list=[S,E,M,T]
        img = make(data_list)
        qr = qr_image()
        qr.Qr_code = img
        img.save("static/media/"+image_name+".png")
    return render(request,"Home.html",{"station":S,"equipment":E,"type":T,"model_number":M,"qr":qr, 'image_name': image_name})









