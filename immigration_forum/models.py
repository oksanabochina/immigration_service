from django.db import models, IntegrityError
from django.contrib.auth.models import User as BaseUser
from ckeditor.fields import RichTextField


class User(BaseUser):
    @property
    def consultantprofile(self):
        try:
            return self.consultantprofile
        except IntegrityError:
            return None

    @property
    def userprofile(self):
        try:
            return self.userprofile
        except IntegrityError:
            return None


class Country(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField()
    snippet = models.CharField(max_length=255)
    flag = models.ImageField(blank=True, null=True, upload_to='images/country/')

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='userprofile')
    bio = models.TextField(max_length=1000)
    profile_pic = models.ImageField(blank=True, null=True, upload_to='images/user_profile/')
    website_url = models.CharField(max_length=255, blank=True, null=True)
    instagram_url = models.CharField(max_length=255, blank=True, null=True)
    facebook_url = models.CharField(max_length=255, blank=True, null=True)
    twitter_url = models.CharField(max_length=255, blank=True, null=True)
    linkedin_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class ConsultantProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='consultantprofile')
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    bio = models.TextField(max_length=1000)
    profile_pic = models.ImageField(blank=True, null=True, upload_to='images/consultant_profile/')
    website_url = models.CharField(max_length=255, blank=True, null=True)
    instagram_url = models.CharField(max_length=255, blank=True, null=True)
    facebook_url = models.CharField(max_length=255, blank=True, null=True)
    twitter_url = models.CharField(max_length=255, blank=True, null=True)
    linkedin_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(ConsultantProfile, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=1)
    body = RichTextField(blank=True, null=True)
    date_posted = models.DateField(auto_now_add=True)
    header_image = models.ImageField(blank=True, null=True, upload_to='images/')
    likes = models.ManyToManyField(User, related_name='posts', null=True)

    def __str__(self):
        return f'{self.title} - by {self.author}'

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment to "{self.post}" - by {self.author}'
