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
        #msg = Contact(name=name,email=email,subject=subject,message=message)
        #msg.save()
        redirect(f"https://api.whatsapp.com/send?phone=923104416475&text=Name%20{name}%20%\n Email%20{email}%20%\n Subject %20{subject} \n Message %20{message}")
        return render(request, "home.html")

