from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, UserProfile
from .forms import LoginForm, PostForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from markdownx.utils import markdownify

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Save User to database
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # Save User Profile to database
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'blog/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return HttpResponse("Your account is disasbled!")
        else:
            print("Invalid login details: {0}".format(username))
            return HttpResponse("Invalid login credentials!")
    else:
        login_form = LoginForm()
        return render(request, 'blog/login.html', {'login_form': login_form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('/')

@login_required
def profile(request):
    userprofile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'blog/profile.html', {'userprofile': userprofile})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-pinned_post', '-published_date')
    for post in posts:
        post.text = markdownify(post.text)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.text = markdownify(post.text)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author or request.user.is_superuser:
        post.delete()
    return redirect('/')
