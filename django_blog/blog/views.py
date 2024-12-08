from .forms import UserUpdateForm, ProfileUpdateForm
from django.core.serializers import serialize
from django.contrib.auth import login, mixins
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .forms import UserCreationForm, UpdateForm, CreateForm, CommentForm
from .models import Post, Comment


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
    template_name = 'blog/view_post.html'
    context_object_name = 'post'


class PostCreateView(CreateView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    model = Post
    form_class = CreateForm
    template_name = 'blog/create_post.html'


class PostUpdateView(UpdateView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    model = Post
    form_class = UpdateForm
    template_name = 'blog/edit_post.html'


class PostDeleteView(DeleteView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    model = Post
    success_url = reverse_lazy('posts')
    template_name = 'blog/delete_post.html'


class CommentListView(ListView):
    model = Comment

    def get(self, request):
        print('REQUEST', request)
        comments = {}
        if request.user.is_authenticated:
            posts = serialize('json', self.model.objects.get(
                post=request.post))  # .reverse()[:10])
        # return render(request, 'home.html', context={'posts': posts})
        return render(request, 'blog/list_post.html', context={'comments': comments})


class CommentDetailView(DetailView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    form_class = CommentForm
    template_name = 'blog/comment_detail.html'


class CommentCreateView(CreateView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    form_class = CommentForm
    template_name = 'blog/comment_create.html'


class CommentUpdateView(UpdateView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    form_class = CommentForm
    template_name = 'blog/comment_update.html'


class CommentDeleteView(DeleteView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    form_class = CommentForm
    template_name = 'blog/comment_delete.html'
