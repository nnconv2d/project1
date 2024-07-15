from django.shortcuts import render
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