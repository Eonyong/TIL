from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    # path('', views.index, name='index'),
    # path('<int:pk>/', views.detail, name='detail'),
    # path('<int:pk>/delete/', views.delete, name='delete'),
    # path('<int:pk>/update/', views.update, name='update'),
]
