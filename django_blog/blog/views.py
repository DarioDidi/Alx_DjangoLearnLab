from .forms import UserUpdateForm, ProfileUpdateForm
from django.core.serializers import serialize
from django.contrib.auth import login, mixins
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .forms import UserCreationForm, UpdateForm, CreatePostForm, CommentForm
from .models import Post, Comment


# from django.contrib.auth.views import LoginView, LogoutView


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})
    # return render(request, 'blog/register.html', {'form': UserCreationForm})# views.py


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'blog/profile.html', context)


class DisplayPosts(ListView):
    model = Post

    def get(self, request):
        posts = serialize('json', self.model.objects.all().reverse()[:10])
        return render(request, 'blog/home.html', context={'posts': posts})


class PostListView(ListView):
    model = Post

    def get(self, request):
        print('REQUEST', request)
        posts = {}
        if request.user.is_authenticated:
            posts = serialize('json', self.model.objects.get(
                author=request.user).reverse()[:10])
        # return render(request, 'home.html', context={'posts': posts})
        return render(request, 'blog/list_post.html', context={'posts': posts})


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    model = Post
    form_class = CreatePostForm
    template_name = 'blog/post_create.html'


class PostUpdateView(UpdateView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    model = Post
    form_class = UpdateForm
    template_name = 'blog/post_edit.html'


class PostDeleteView(DeleteView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    model = Post
    success_url = reverse_lazy('posts')
    template_name = 'blog/post_delete.html'


class CommentListView(ListView):
    model = Comment

    def get(self, request):
        print('REQUEST', request)
        comments = {}
        if request.user.is_authenticated:
            posts = serialize('json', self.model.objects.get(
                post=request.post))  # .reverse()[:10])
        # return render(request, 'home.html', context={'posts': posts})
        return render(request, 'blog/comment_list.html', context={'comments': comments})


class CommentDetailView(DetailView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_detail.html'


class CommentCreateView(CreateView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_create.html'

    def dispatch(self, request, *args, **kwargs):
        comment = self.get_object()
        if request.user != comment.post.author:
            return HttpResponseForbidden("You do not have permission to access this resource.")
        return super().dispatch(request, *args, **kwargs)


class CommentUpdateView(UpdateView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_update.html'
    success_url = reverse_lazy('blog_post_detail')

    def dispatch(self, request, *args, **kwargs):
        comment = self.get_object()
        if request.user != comment.post.author:
            return HttpResponseForbidden("You do not have permission to access this resource.")
        return super().dispatch(request, *args, **kwargs)


class CommentDeleteView(DeleteView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_delete.html'

    def dispatch(self, request, *args, **kwargs):
        comment = self.get_object()
        if request.user != comment.post.author:
            return HttpResponseForbidden("You do not have permission to access this resource.")
        return super().dispatch(request, *args, **kwargs)


# class SearchView(ListView):
#     model = Post
#     template_name = 'blog/search_post.html'

#     def get_queryset(self):
#         search_term = self.request.GET.get('search_term')
#         title_q = Q(title__icontains=search_term) if search_term else Q()
#         content_q = Q(content__icontains=search_term) if search_term else Q()
#         tag_q = Q(tags__icontains=search_term) if search_term else Q()
#         combined_q = title_q & content_q & tag_q
#         return Post.objects.filter(combined_q)


def search_view(request):
    search_term = request.GET.get('search_term')
    title_q = Q(title__icontains=search_term) if search_term else Q()
    content_q = Q(content__icontains=search_term) if search_term else Q()
    tag_q = Q(tags__icontains=search_term) if search_term else Q()
    combined_q = title_q & content_q & tag_q

    if search_term:
        results = Post.objects.filter(Q(search_term))
        return render(request, 'blog/search_results.html', {'results': results})
    return render(request, 'blog/search_post.html')


class PostByTagListView(ListView):
    context_object_name = 'posts'
    template_name = 'blog/tagged_posts.html'  # adjust to your template name

    def get_queryset(self):
        tag = self.kwargs['tag']  # retrieve the tag slug from the URL
        return Post.objects.filter(Q(tags__name__icontains=tag))
