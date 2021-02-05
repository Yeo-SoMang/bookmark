from django.shortcuts import render, redirect, get_object_or_404
from .models import Bookmark
from .forms import BookmarkForm
#get object or 404 = 원하는 내용이 없다면 404를 보냄
def list(request):
    list = Bookmark.objects.all()

    return render(request, 'bookmark/list.html', {
        'list':list,
    })

# def new(request):
#     if request.method == 'POST':
#         form = BookmarkForm(request.POST)
#         #만약 폼에 내용이 있다면.
#         if form.is_vaild():
#             #북마크에 데이터베이스(테이블)를 지정
#             bookmark = Bookmark()
#             #form으로 받은 cleaned 데이터를 통해 내용을 정리하고 site_name을 정리
#             bookmark.site_name = form.cleaned_data['site_name']
#             #from으로 받은 url을 집어넣음
#             bookmark.url = form.cleaned_data['url']
#             #저장
#             bookmark.save()
#             #bookmark의 list로 보냄
#             return redirect('bookmark:list')
#         #esle post방식으로 들어오지 않았다면
#         else:
#             #form에 기본 틀을 담고
#             form = BookmarkForm()
#         return render(request, 'bookmark/new.html', {
#             'form': form,
#         })

def new(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            bookmark = Bookmark()
            bookmark.site_name = form.cleaned_data['site_name']
            bookmark.url = form.cleaned_data['url']
            bookmark.save()
            return redirect('bookmark:list')
    else:
        form = BookmarkForm()
    return render(request, 'bookmark/new.html', {
        'form': form,
    })

# #아무 글이나 수정을하면 안되니까 primary key
# def edit(request, pk):
#     #get_object_or_404를 통해 데이터베이스의 내용을 조회, 기준은 전달받은 pk값
#     bookmark = get_object_or_404(Bookmark, pk=pk)
#     #만약에 메소드가 Post로 왔다면
#     if request.method == 'POST':
#         #form에다가 북마크폼의 리퀘스트 포스트로 받은 내용을 넣음.
#         #에디트는 기존에 있던 값을 뿌려줘야해서 인스턴스를 지정해 북마크를 가져옴
#         form = BookmarkForm(request.POST, instance=bookmark)
#         #만약에 form의 값이 있다면
#         if form.is_vaild():
#             #bookmark의 site name값은 form으로 받은 site_name을 넣음
#             bookmark.site_name = form.cleaned_data['site_name']
#             #bookmark_urlfile의 form에서받은 url 값을 넣음
#             bookmark.url = form.cleaned_data['url']
#             bookmark.save()
#             #특정 페이지를 다시 돌려보냄
#             return redirect('bookmark:list')
#         #post 값이 없다면 기본페이지를 보여줌
#         else:
#             form = BookmarkForm(instance=bookmark)
#         #어떤 html파일을 쓸건지
#         return render(request, 'bookmark/edit.html', {
#             # 보낼 내용
#             'bookmark' : bookmark,
#             'form' : form,
#         })

def edit(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)

    if request.method =='POST':
        form = BookmarkForm(request.POST, instance=bookmark)
        if form.is_valid():
            bookmark.site_name = form.cleaned_data['site_name']
            bookmark.url = form.cleaned_data['url']
            bookmark.save()
            return redirect('bookmark:list')
    else:
        form = BookmarkForm(instance=bookmark)
    return render(request, 'bookmark/edit.html', {
        'bookmark': bookmark,
        'form': form,
    })


def delete(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)

    if request.method == 'POST':
        bookmark.delete()
        return redirect('bookmark:list')


