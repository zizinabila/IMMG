from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.utils.text import slugify
from .models import Post, Category
from master.models import Organization
from django.contrib.auth.models import User
from .forms import PostCreateForm
from django.contrib.auth.decorators import permission_required, login_required

def home(request):
    context = {
        'posts': 'test'
    }
    return render(request, 'blog/home.html', context)


def PostList(request):
    post_list = Post.objects.filter(is_posted=True).order_by('-date_posted')
    paginator = Paginator(post_list, 6) # Show 6 post per page

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/home.html', {'posts': posts})

def PostUserList(request, username):
    user = get_object_or_404(User, username=username)
    post_list = Post.objects.filter(author=user).order_by('-date_posted')
    paginator = Paginator(post_list, 6) # Show 6 post per page

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/user_posts.html', {'posts': posts, 'username': username})

def PostCategoryList(request, slug):
    category = get_object_or_404(Category, slug=slug)
    post_list = Post.objects.filter(category=category).order_by('-date_posted')
    paginator = Paginator(post_list, 6) # Show 6 post per page

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/category_posts.html', {'posts': posts, 'category': category.category_desc})

def PostDetail(request,slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

# def PostOrganizationList(request):
#     organization = Organization.objects.all().order_by('report_to')
#     return render(request, 'blog/post_organization.html', {'organization':organization})


@login_required
@permission_required('blog.add_post', login_url="permission-page")
def PostCreate(request):
    if request.method == 'POST':
        posts = Post.objects.filter(title__iexact=request.POST['title'])
        if posts.exists():
            messages.error(request, 'Title : "{}" already exist in database!'.format(request.POST['title']))
            form = PostCreateForm(request.POST)
        else:
            form = PostCreateForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = User.objects.get(username=request.user.username)  # use your own profile here
                post.save()
                messages.success(request, f'Your post has been created and waiting for approval!')
                return redirect('home')
    else:
        form = PostCreateForm()

    context = {
        'form': form
    }

    return render(request, 'blog/post_form.html', context)

def Permission(request):
    return render(request, 'blog/permission.html')
