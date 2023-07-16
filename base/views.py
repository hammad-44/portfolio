from django.shortcuts import render
from base.models import Contact
# Create your views here.

def index(request):
    return render(request, "home.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        msg = Contact(name=name,email=email,subject=subject,message=message)
        msg.save()
        return render(request, "home.html")

