from django.shortcuts import render

from .models import Participants,ParticipantsAdmin
# Create your views here.
def home(request):
    context={}
    return render(request,"eventapp/home.html",context)

def reg(request):
    context={}
    if request.method == 'POST':
        p1 = Participants()
        p1.username = request.POST.get('username','-')
        p1.email= request.POST.get ('email','-')
        p1.contnum=request.POST.get('contnum','000') 
        p1.inst= request.POST.get('inst','-')

        if len(Participants.objects.all())>15: 
            return render(request,'eventapp/fail.html') 
        else:
            p1.save()
            return render(request,'eventapp/success.html',context)  
    if request.method == 'GET':
        context['username']=''
        context['email']=''
        context['contnum']=''
        context['inst']=''

    return render(request,"eventapp/register.html",context)
    
def lop(request):
    context={}
    context['participants']= Participants.objects.all()
    return render(request,"eventapp/listofpart.html",context)
    
