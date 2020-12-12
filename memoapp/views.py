from django.shortcuts import render, get_object_or_404, redirect
from .models import Memo

def index(request):
    return render(request, 'memoapp/index.html')

def edit(request):
    return render(request, 'memoapp/edit.html')

def new(request):
    return render(request, 'memoapp/new.html')

def create(request):
    title = request.POST['title']
    image = None
    if 'image' in request.FILES:
        image = request.FILES['image']
    content = request.POST['content']

    memo = Memo(title = title, image = image, content = content)
    memo.save()
    return redirect('/table/')

def table(request):
    memos = Memo.objects.all()
    return render(request, 'memoapp/table.html', {'memos': memos})

def detail(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    return render(request, 'memoapp/detail.html', {'memo': memo})