from django.shortcuts import render,redirect
from django.contrib import messages
from portfolio.models import Contact,Blogs

# Create your views here.
def home(request):
    return render(request,'home.html')

def handleblog(request):
    posts=Blogs.objects.all()
    context={"posts":posts}
    return render(request,'handleblog.html',context)

def about(request):
    return render(request,'about.html')

def internshipdetails(request):
    return render(request,'intern.html')



def contact(request):
    if request.method=="POST":
        fname=request.POST.get('name')
        fusn=request.POST.get('usn')
        femail=request.POST.get('email')
        fphoneno=request.POST.get('num')
        fcollegename=request.POST.get('cname')
        fdesc=request.POST.get('desc')
        query=Contact(name=fname,usn=fusn,email= femail,phonenumber=fphoneno,Collegename=fcollegename,description=fdesc)
        query.save()
        messages.info(request,"contact saved successfully we well contact to u soon..")
       
        
        return redirect('/contact')        

    return render(request,'contact.html')