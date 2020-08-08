from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, Http404
from blog.models import Post
from .forms import PostForm

# Create your views here.

# def my_view(request):
#     return HttpResponse("Hello this is raj kumar's website")


def post_list(request):
    posts = Post.objects.all()
    return render(request,'blog/post_list.html', {'posts':posts})


def post_details(request,pk):
    #post=get_object_or_404(Post,pk=pk)
    try:
        post = Post.objects.get(pk=pk)
        return render(request,'blog/post_details.html',{'post':post})
    except:
        raise Http404('post does not exsist')

def new_post(request):
    if request.method == "POST":
        form=PostForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

