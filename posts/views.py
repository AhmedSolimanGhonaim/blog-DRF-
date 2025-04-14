from rest_framework import generics
from django.contrib.auth import get_user_model
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly



class PostBaseView:
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostList(PostBaseView, generics.ListCreateAPIView):
    pass


class PostDetail(PostBaseView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)



class UserBaseView:
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserList(UserBaseView, generics.ListCreateAPIView):
    pass


class UserDetail(UserBaseView, generics.RetrieveUpdateDestroyAPIView):
    pass
