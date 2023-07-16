from django.shortcuts import render,redirect
from blog.models import Post, BlogComment
from django.contrib import messages

# Create your views here.
def blogHome(request): 
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, "allblogs.html", context)

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    post.views= post.views +1
    post.save()
    comments= BlogComment.objects.filter(post=post)

    context={'post':post, 'comments': comments}
    return render(request, "singlepost.html", context)

def postComment(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        comment=request.POST.get('comment')
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)      
        comment=BlogComment(name=name, email=email,comment= comment, post=post)    
        comment.save()
        return redirect(f"/blog/{post.slug}")

