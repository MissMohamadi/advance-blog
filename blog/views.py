from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, FormView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from .models import Post
from .forms import PostForm



class IndexView(TemplateView):

    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Marzieh'
        return context

class PostListView(ListView):
    # model = Post
    # queryset = Post.objects.all()
    def get_queryset(self):
        posts= Post.objects.filter(status=True)
        return posts
    context_object_name = 'posts'
    paginate_by = 2

class PostDetailView(DetailView):
    model = Post

'''
class PostCreateView(FormView):
    template_name = "contact.html"
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
'''
class PostCreateView(CreateView):
    model = Post
    # fields = ['title', 'content', 'status', 'author', 'category', 'published_date']
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = "/blog/post/"