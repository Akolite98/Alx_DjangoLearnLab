from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post, Comment, Tag
from .forms import CommentForm
from taggit.models import Tag
from django.db.models import Q
import importlib

forms = importlib.import_module("blog.forms")
CommentForm = forms.CommentForm

# Post List View with Tag Filtering
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5 

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_name = self.request.GET.get('tag')
        if tag_name:
            queryset = queryset.filter(tags__name__iexact=tag_name)
        return queryset

# Post Detail View with Tags
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.object.tags.all()
        return context

# Post Create View with Tag Handling
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        tags = self.request.POST.get('tags')
        if tags:
            tag_list = [tag.strip() for tag in tags.split(',')]
            form.instance.tags.set(tag_list)
        return response

# Post Update View with Tag Handling
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        tags = self.request.POST.get('tags')
        if tags:
            tag_list = [tag.strip() for tag in tags.split(',')]
            form.instance.tags.set(tag_list)
        return response

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Post Delete View
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Comment Create View
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()

# Comment Update View
class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)

    def get_success_url(self):
        return self.object.post.get_absolute_url()

# Comment Delete View
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)

    def get_success_url(self):
        return self.object.post.get_absolute_url()

# Search Posts View
def search_posts(request):
    query = request.GET.get('q')
    posts = Post.objects.all()

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()

    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})
class PostByTagListView(ListView):
    model = Post
    template_name = "blog/post_list.html"  # Adjust to your template
    context_object_name = "posts"

    def get_queryset(self):
        tag_slug = self.kwargs.get('tag_slug')
        tag = get_object_or_404(Tag, slug=tag_slug)
        return Post.objects.filter(tags__in=[tag])  # Filtering posts by tag

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = get_object_or_404(Tag, slug=self.kwargs.get("tag_slug"))
        return context
