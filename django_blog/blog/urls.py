from django.urls import path
from blog.views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, DisplayPosts, profile, register
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', DisplayPosts.as_view(), name='home'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/new', PostCreateView.as_view(), name='create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit', PostUpdateView.as_view(), name='update'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='delete'),
]