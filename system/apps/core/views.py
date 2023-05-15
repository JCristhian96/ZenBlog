from typing import Any, Dict
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, RedirectView, FormView, DetailView, ListView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
# 
from .models import Post, Category, Favorite


class IndexView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_first"] =  Post.objects.first()
        context["posts_1"] =  Post.objects.all()[0:3]
        context["posts_2"] =  Post.objects.all()[3:6]
        context["posts_recents"] =  Post.objects.all()[0:6]
        return context
    

class PostDetailView(DetailView):
    model = Post
    template_name = "detail.html"
    context_object_name = "post"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        context["categories"] = Category.objects.all()
        if self.request.user.is_authenticated:
            context["favorite"] = Favorite.objects.filter(user=self.request.user, post=self.object).exists()
        else:
            context["favorite"] = False
        return context
    

class PostListView(ListView):
    model = Post
    template_name = "list.html"
    context_object_name = "posts"   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()        
        return context


class FavoriteListView(LoginRequiredMixin, ListView):
    model = Favorite
    template_name = "favorites.html"
    context_object_name = "favorites"   
    
    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)
    
        
class PostEditView(RedirectView):
    url = reverse_lazy('core:index')
    
    def get_redirect_url(self, *args, **kwargs):
        self.url = self.request.META['HTTP_REFERER']
        if self.request.user.is_authenticated:
            post = get_object_or_404(Post, pk=kwargs['pk'])
            if kwargs['action'] == 'add':
                Favorite.objects.create(user=self.request.user, post=post)
            if kwargs['action'] == 'delete':
                Favorite.objects.filter(user=self.request.user, post=post).delete()
            
        return super().get_redirect_url(*args, **kwargs)
     
    
class AboutView(TemplateView):
    template_name = "about.html"


class ContactView(TemplateView):
    template_name = "contact.html"
    
    
class LoginView(FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('core:index')   
    template_name = "login.html" 
    
    def get_initial(self):
        initial = super(LoginView, self).get_initial()
        initial.update({'username': "demo"})
        return initial
        
    def form_valid(self, form):
        if form.is_valid():
            login(self.request, form.get_user())
        return super().form_valid(form)
        
    
class LogoutView(RedirectView):
    url = reverse_lazy('core:index')
    
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return super().get_redirect_url(*args, **kwargs)