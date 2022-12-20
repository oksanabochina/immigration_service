from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from immigration_api.permissions import IsAuthorOrReadOnly, IsAdminOrReadOnly
from immigration_api.serializers import PostSerializer, CommentSerializer, ConsultantProfileSerializer, \
    PostWithCountrySerializer, CountrySerializer, UserProfileSerializer
from immigration_forum.models import Post, Comment, ConsultantProfile, Country, UserProfile


class PostViewSet(ModelViewSet):
    queryset = Post.objects.select_related('country').select_related('author').all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['author', 'country']
    search_fields = ['title', 'body']
    permission_classes = [IsAuthorOrReadOnly]

    def get_serializer_context(self):
        author_id = self.request.user.consultantprofile.id if hasattr(self.request.user, 'consultantprofile') else None
        return {'author_id': author_id}

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return PostSerializer
        return PostWithCountrySerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['author']
    search_fields = ['body']
    # http_method_names = ['GET', 'HEAD', 'OPTIONS' 'POST', 'DELETE']

    def get_serializer_context(self):
        return {
            'post_id': self.kwargs['post_pk'],
            'author_id': self.request.user.id,
        }

    def get_queryset(self):
        return Comment.objects.select_related('post').select_related('author').filter(post_id=self.kwargs['post_pk'])

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        if self.request.method in ['DELETE', 'PUT', 'PATCH']:
            return [IsAdminUser()]
        return [AllowAny()]


class ConsultantProfileViewSet(ModelViewSet):
    queryset = ConsultantProfile.objects.select_related('user').select_related('country').all()
    serializer_class = ConsultantProfileSerializer
    permission_classes = [IsAdminUser]


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.select_related('user').all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAdminUser]


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAdminOrReadOnly]
