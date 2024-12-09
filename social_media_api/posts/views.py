from django.core.exceptions import PermissionDenied
from django.contrib.auth import mixins
from django.db.models import Q
from django.shortcuts import render

from rest_framework import filters
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment


class PostPagination(PageNumberPagination):
    page_size = 10  # Adjust the page size as needed
    page_size_query_param = 'page_size'
    max_page_size = 100


# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostListView(generics.ListAPIView):
    # queryset = Post.objects.all()
    # serializer_class = PostSerializer
    pagination_class = PostPagination
    filter_backends = [filters.SearchFilter]

    def get(self, request):
        posts = Post.objects.all()
        paginated_posts = PostPagination().paginate_queryset(
            queryset=posts, request=request)
        serializer = PostSerializer(paginated_posts, many=True)
        return Response(serializer.data)


class PostCreateView(APIView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    serializer_class = PostSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostUpdateView(APIView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    def post(self, request):
        serializer = PostSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            post = Post.objects.get(id=request.data['id'])
            if post.author == request.user:
                serializer.update(post, serializer.validated_data)
                return Response(serializer.data)
        return Response(serializer.errors, status=400)


class PostDetailView(APIView):
    def get(self, request):
        # Handle GET request
        post = Post.objects.get(id=request.data['id'])
        serializer = PostSerializer(post)
        return Response(serializer.data)


class PostDeleteView(generics.DeleteAPIView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def delete(self, request, pk):
        post = self.get_object(pk)
        if post.author == request.user:
            post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostSearchView(generics.ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self, request):
        search_term = request.GET.get('search_term')
        title_q = Q(title__icontains=search_term) if search_term else Q()
        content_q = Q(content__icontains=search_term) if search_term else Q()
        # combined_q = title_q & content_q
        results = Post.objects.filter(title_q).filter(content_q)
        return results


class CommentPagination(PageNumberPagination):
    page_size = 20  # Adjust the page size as needed
    page_size_query_param = 'page_size'
    max_page_size = 100


class CommentListView(generics.APIView):
    pagination_class = CommentPagination
    filter_backends = [filters.SearchFilter]

    def get(self, request, **kwargs):
        pk = self.kwargs['pk']
        post = Post.objects.get(id=pk)
        comments = Comment.objects.filter(post=post)
        paginated_comments = CommentPagination().paginate_queryset(
            queryset=comments, request=request)
        serializer = CommentSerializer(paginated_comments, many=True)
        return Response(serializer.data)


class CommentCreateView(APIView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    serializer_class = CommentSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentUpdateView(APIView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    def post(self, request):
        serializer = CommentSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            comment = Comment.objects.get(id=request.data['pk'])
            if self.user != request.user:
                raise PermissionDenied(
                    'Only the author can edit or delete this post')
            if comment.author == request.user:
                serializer.update(Comment, serializer.validated_data)
                return Response(serializer.data)
        return Response(serializer.errors, status=400)


class CommentDetailView(APIView):
    def get(self, request):
        # Handle GET request
        comment = Comment.objects.get(id=request.data['id'])
        serializer = CommentSerializer(comment)
        return Response(serializer.data)


class CommentDeleteView(generics.DeleteAPIView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def delete(self, request, pk):
        comment = self.get_object(pk)
        if request.user == comment.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
