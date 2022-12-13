from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from immigration_api.serializers import PostSerializer, CommentSerializer, ConsultantProfileSerializer, \
    PostWithCountrySerializer, CountrySerializer, UserProfileSerializer
from immigration_forum.models import Post, Comment, ConsultantProfile, Country, UserProfile


class PostViewSet(ModelViewSet):
    queryset = Post.objects.select_related('country').select_related('author').all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['author', 'country']
    search_fields = ['title', 'body']

    def get_serializer_context(self):
        return {'author_id': self.request.user.consultantprofile.id}

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return PostSerializer
        return PostWithCountrySerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['author']
    search_fields = ['body']

    def get_serializer_context(self):
        return {
            'post_id': self.kwargs['post_pk'],
            'author_id': self.request.user.id,
        }

    def get_queryset(self):
        return Comment.objects.select_related('post').select_related('author').filter(post_id=self.kwargs['post_pk'])


class ConsultantProfileViewSet(ModelViewSet):
    queryset = ConsultantProfile.objects.select_related('user').select_related('country').all()
    serializer_class = ConsultantProfileSerializer


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.select_related('user').all()
    serializer_class = UserProfileSerializer


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
