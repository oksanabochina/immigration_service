from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from immigration_forum.models import Post, Comment, ConsultantProfile, Country, UserProfile


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'country', 'date_posted', 'body']

    author = serializers.StringRelatedField()

    def create(self, validated_data):
        author_id = self.context['author_id']
        return Post.objects.create(author_id=author_id, **validated_data)


class PostWithCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'country', 'date_posted', 'body']

    author = serializers.StringRelatedField()
    country = serializers.StringRelatedField()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'body', 'date_added']

    post = serializers.StringRelatedField()
    author = serializers.StringRelatedField()

    def create(self, validated_data):
        post_id = self.context['post_id']
        author_id = self.context['author_id']
        return Comment.objects.create(post_id=post_id, author_id=author_id, **validated_data)


class ConsultantProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultantProfile
        fields = [
            'id', 'user_id', 'country', 'bio', 'website_url', 'instagram_url', 'facebook_url', 'twitter_url',
            'linkedin_url',
        ]

    country = serializers.StringRelatedField()
    user_id = serializers.IntegerField()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'id', 'user_id', 'bio', 'website_url', 'instagram_url', 'facebook_url', 'twitter_url', 'linkedin_url',
        ]
    user_id = serializers.IntegerField()


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'snippet', 'info']


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'first_name', 'last_name']