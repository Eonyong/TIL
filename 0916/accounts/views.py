from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, update_session_auth_hash, get_user_model
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserChangeForm
from IPython import embed

# Create your views here.

def user_list(request):
    User = get_user_model()
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request, 'accounts/user_list.html', context)
    

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            auth_login(request, request.user())
            return redirect('articles:index')

    else:
        form = UserCreationForm()
    
    context = {
        'form':form
    }
    
    return render(request, 'accounts/auth_form.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect(request.GET.get('next') or 'articles:index')
                # request.GET.get('next') 는 주소/next의 다음 부분 전부(articles/<int:pk>/update)를 들고오는고임

        else:
            form = AuthenticationForm()
        
        context = {
            'form':form
        }
        
        return render(request, 'accounts/auth_form.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

@login_required
@require_POST
def delete(request):
    if request.user.is_athenticated:
        request.user.delete()
    return redirect('articles:index')

@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')

    else:
        form = CustomUserChangeForm(instance=request.user) # 이 친구를 그냥 사용하면 그이 운영자 마냥 사용이 가능하므로 수정해야함

    context = {
        "form" : form,
    }
    return render(request, 'accounts/auth_form.html', context)

@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)