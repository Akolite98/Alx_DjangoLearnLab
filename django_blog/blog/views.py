from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import CommentForm
from taggit.models import Tag
from django.db.models import Q
from .models import Post



# Existing PostListView
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

# Existing PostDetailView
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.object.tags.all()  # Fetch tags for the post
        return context

# Ensure PostCreateView is defined
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)  # Save post first

        # Handle tags (if using django-taggit)
        tags = self.request.POST.get('tags')
        if tags:
            tag_list = [tag.strip() for tag in tags.split(',')]
            form.instance.tags.set(tag_list)  # Assign tags

        return response


# Existing PostUpdateView
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        # Update tags
        tags = self.request.POST.get('tags')
        if tags:
            tag_list = [tag.strip() for tag in tags.split(',')]
            form.instance.tags.set(tag_list)

        return response


# Existing PostDeleteView
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the logged-in user as the author
        form.instance.post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()  # Redirect to the post after adding a comment


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)  # Ensure only the author can edit

    def get_success_url(self):
        return self.object.post.get_absolute_url()


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'
    success_url = reverse_lazy('post_list')  

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)  # Ensure only the author can delete

    def get_success_url(self):
        return self.object.post.get_absolute_url()

        
def search_posts(request):
    query = request.GET.get('q')  # Get search query from request
    posts = Post.objects.all()

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |  # Search in title
            Q(content__icontains=query) |  # Search in content
            Q(tags__name__icontains=query)  # Search in tags (if using django-taggit)
        ).distinct()

    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})
