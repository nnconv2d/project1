from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def blog(request):
    # 모든 Post를 가져와 postlist에 저장
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때 postlist를 가져옴
    return render(request, 'main/blog.html', {'postlist': postlist})

# blog의 게시글을 불러옴
def posting(request, pk):
    # 게시글 중 pk(primary key)를 이용해 하나의 게시글을 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열면 찾아낸 게시글을 post라는 이름으로 가져옴
    return render(request, 'main/posting.html', {'post':post})

def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article = Post.objects.create(
                postname = request.POST['postname'],
                contents = request.POST['contents'],
                mainphoto = request.POST['mainphoto'],
            )
        else:
            new_article = Post.objects.create(
                postname = request.POST['postname'],
                contents = request.POST['contents'],
                mainphoto = request.POST['mainphoto'],
            )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', {'Post':post})