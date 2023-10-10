from django.shortcuts import render,redirect
from base.models import Contact
# Create your views here.
from blog.models import Post, BlogComment

def index(request):
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, "home.html",context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        msg = Contact(name=name,email=email,subject=subject,message=message)
        msg.save()
        redirect(f"https://api.whatsapp.com/send?phone=923104416475&text=Name%20{name}%20%\n Email%20{email}%20%\n Subject %20{subject} \n Message %20{message}")
        return render(request, "home.html")

