from django.urls import path
# from blog.views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, DisplayPosts, profile, register
from blog.views import *
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
     path('', DisplayPosts.as_view(), name='home'),
     path('register/', register, name='register'),
     path('login/', LoginView.as_view(), name='login'),
     path('logout/', LogoutView.as_view(), name='logout'),
     path('profile/', profile, name='profile'),
     path('posts/', PostListView.as_view(), name='posts'),
     path('post/new', PostCreateView.as_view(), name='create_post'),
     path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
     path('post/<int:pk>/update', PostUpdateView.as_view(), name='update_post'),
     path('post/<int:pk>/delete', PostDeleteView.as_view(), name='delete_post'),
     path('/post/<int:pk>/comments/new/',
         CommentCreateView.as_view(), name='create_comment'),
     path('comment/<int:pk>/update/',
         CommentUpdateView.as_view(), name='update_comment'),
     path('comment/<int:pk>/delete/',
         CommentDeleteView.as_view(), name='delete_comment'),
     path('comment/<int:pk>/',
         CommentDetailView.as_view(), name='view_comment'),
     path('blog/tag/<slug:tag_slug>/',
          TagPostView.as_view(), name='tag_posts'),
]

#  ["post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/"
