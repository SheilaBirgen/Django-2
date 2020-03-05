from django.shortcuts import render,redirect,
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import Image, Comment, Profile, Followers


# Create your views here.
def registration(request):
    if request.method == 'Post':
        form = Register(request.POST)
        if form.is valid():
            username = form.cleaned_data.get('username')
            form.save()

            username =form.cleaned_data('username')
            email = form.cleaned_data('email')
            password = form.cleaned_data('password')
            recipient = User(username=username,email=email)
            try:
                send_welcome_email(username,email)
                message.success(request, f'Account has been created successfully!')
            except:
                print('error')
            return redirect('login')
    else:
        form=RegisterForm()
    contect = {
        'form':form,
    }     
    return render(request,'users/register.html', context)   

@login_required
def image(request)
    image = image.objects.all()
    users = User.objects.exclude(id=request.user.id)
    following = Following.objects.get(current_user=request.user)
    followters = followinf.users.all()
    comments = Comment.objects.all()
    comment_form = CommentForm()
    context = {
        'image':image,
        'comment_form':comment_form,
        'comments':comments,
        'users':users,
        'followers':followers,
    }
    return render(request,'posts.html', context)
 