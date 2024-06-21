from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib import messages

def login_blog(request):
    if request.method == "POST":
        username = request.POST["username"] 
        pwd = request.POST["pwd"] 
        print ('le nom est:',username)
        user= authenticate(username=username,password=pwd)
        if user is not None:
            return redirect("home")
            
        else: 
            messages.error(request, "Erreur d'autantification")
            return render(request,"login.html")
    return render(request,"login.html")