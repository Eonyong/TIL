from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
from IPython import embed   # dajngo 에쓰는 디버깅 툴

# Create your views here.
@require_safe
def index(request):
    # embed()

    if request.session:
        # 로그인 했을 경우
        visits_num = request.session.get('visits_num', 0)
        request.session['visits_num'] = visits_num + 1
    else:
        visits_num = 0

    articles = Article.objects.order_by('-pk')
    
    context = {
        'articles': articles,
        'visits_num' : visits_num,
    }
    return render(request, 'articles/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    if request.user.is_athenticated:
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:login')
        


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
