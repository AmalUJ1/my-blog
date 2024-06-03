# importing models and libraries
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, PostForm, CustomLoginForm 

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'blog/register.html', {'form': form})

def read_me(request):
    return render(request, 'blog/read_me.html')

def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a personalized home page
    else:
        form = CustomLoginForm()
    return render(request, 'blog/custom_login.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home or post detail page after updating
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/update_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'blog/delete_post.html', {'post': post})

# class based views for posts
class PostsList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
 
# class based view for each post
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def home(request):
    posts = Post.objects.filter(author=request.user)
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context) 

def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': all_posts})

def about(request):
    return render(request, 'blog/about.html')
def privacy(request):
    return render(request, 'blog/privacy.html')
def tos(request):  
    return render(request, 'blog/tos.html')
