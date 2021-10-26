from django.shortcuts import redirect, render

from mycrud.forms import UserForm
from mycrud.models import User

# Create your views here.

def home(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form=UserForm()
    data=User.objects.all()
    return render(request,'home.html',{'form':form ,'data':data})

def delete(request,id):
    user=User.objects.get(pk=id)
    user.delete()
    return redirect('/')

def update(request,id):
    if request.method=="POST":
        data=User.objects.get(pk=id)
        form=UserForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        data=User.objects.get(pk=id)
        form=UserForm(instance=data)
    
    return render(request,'update.html',{'form':form})