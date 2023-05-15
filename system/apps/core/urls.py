from django.urls import path
#
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<pk>/', views.PostDetailView.as_view(), name='post'),
    path('post/edit/<pk>/<action>/', views.PostEditView.as_view(), name='edit'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('favorites/', views.FavoriteListView.as_view(), name='favorites'),
    
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    #
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
