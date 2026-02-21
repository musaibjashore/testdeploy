from django.shortcuts import render,get_object_or_404
# Create your views here.
from django.views.generic import ListView, DetailView,CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy,reverse
from .models import Post,Comment
from django.contrib.auth.models import User


class homepage(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'

class postview(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'indiv_posts'
    

class CommentView(CreateView):
    model = Comment
    template_name = 'comment.html'
    fields = ('comment',)

    def form_valid(self, form):
        form.instance.post = get_object_or_404(Post,pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        return super().form_valid(form)



class newpost(CreateView):
    model=Post
    template_name = 'post_new.html'
    fields = ('title','body','img')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class editpost(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body','img']

class deletepost(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'users'
    
    
    
