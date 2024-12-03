from .forms import UserUpdateForm, ProfileUpdateForm
from django.core.serializers import serialize
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import UserCreationForm
from .models import Post


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.post)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": UserCreationForm})
    # return render(request, "blog/register.html", {"form": UserCreationForm})# views.py


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
    return render(request, 'profile.html', context)


class DisplayPosts(ListView):
    model = Post

    def get(self, request):
        posts = serialize("json", self.model.objects.all().reverse()[:10])
        return render(request, "home.html", context={'posts': posts})


class UserPosts(ListView):
    model = Post

    def get(self, request):
        print("REQUEST", request)
        posts = {}
        if request.user.is_authenticated:
            posts = serialize("json", self.model.objects.get(author=request.user).reverse()[:10])
        return render(request, "home.html", context={'posts': posts})
