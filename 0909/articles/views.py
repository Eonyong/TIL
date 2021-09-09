from articles.models import Article
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_http_methods
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.all()[::-1]

    context = {
        'articles':articles,
    }

    return render(request, 'articles/index.html', context)

@require_http_methods(["GET", "POST"])
def create(request):
    if request.method =='POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # add_message
            # messages.add_message(request, messages.INFO, '게시글이 생성되었습니다.....')
            messages.info(request, '게시글이 생성.!.!.!')

            return redirect('articles:index')

    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article':article,
    }
    return render(request, 'articles/detail.html', context)

@require_http_methods(["GET", "POST"])
def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save()
            messages.info(request, '게시글이 수정.!.!.!')
            return redirect('articles:detail', article.pk)
    
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    messages.warning(request, '게시글이 삭제.!.!.!')

    return redirect('articles:index')
