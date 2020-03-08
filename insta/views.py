from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment, Profile, Following


# Create your views here.
def registration(request):
    if request.method == 'Post':
        form = Register(request.POST)
        if form.is_valid():
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
def post(request):
    posts = Post.objects.all()
    users = User.objects.exclude(id=request.user.id)
    following = Following.objects.get(current_user=request.user)
    followers = followers.users.all()
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

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, f'You post have been created successfully!!')
            return redirect('posts')
    else:
        form = PostForm()
    context = {
        "form":form,
    }
    return render(request, 'post_create.html', context)

@login_required
def comment(request, post_id):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            post = Post.get_post(post_id)
            comment.post = post
            comment.save()
            return redirect('posts')
    else:
        comment_form = CommentForm()
    context = {
        "comment_form":comment_form,
    }
    return render(request, 'posts.html', context)
@login_required
def commenting(request, post_id):
    posts = Post.objects.get(pk=post_id)
    context ={
        "posts":posts,
    }
    return render(request, 'comments.html', context)
