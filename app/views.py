from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *
from app.forms import StudentForm

#Function Base View for returning httpresponse.
def fbv_string(request):
    return HttpResponse('<h1>This is fbv_string page</h1>')

#Class Base View for returning httpresoponse.
class cbv_string(View):
    def get(self,request):
        return HttpResponse('<h1>This is cbv_string page</h1>')

#FBV for rendering html page.
def fbv_page(request):
    return render(request,'fbv_page.html')

#CBV for rendering html page.
class cbv_page(View):
    def get(self,request):
        return render(request,'cbv_page.html')
    

#FBV for inserting data.
def Insert_fbv(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data inserted successfully in fbv')
        
    return render(request,'Insert_fbv.html',d)



#CBV for inserting data.
class Insert_cbv(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'Insert_cbv.html',d)
    
    def post(self,request):
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data inserted successfully in cbv')
        
#Template view for class base view
class Cbv_Temp(TemplateView):
    template_name='Cbv_Temp.html'
    
    
