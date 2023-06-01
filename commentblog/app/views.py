from django.shortcuts import render, redirect
from .models import Post, Comment
# Create your views here.

def home(request):
    posts=Post.objects.all()

    return render(request, 'home.html', {'posts':posts})

def new(request):
    if request.method =='POST':
        new_post = Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content']
        )
        return redirect('detail', new_post.pk)
    return render(request, 'new.html')

def detail(request, post_pk):
    post=Post.objects.get(pk=post_pk)
    print(post)

    #댓글 작성을 위한 요청처리
    if request.method=='POST':

        Comment.objects.create(
            post=post,
            content = request.POST['content']
        )

    return render(request, 'detail.html', {'post':post})