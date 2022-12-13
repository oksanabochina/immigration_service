from django.urls import path, include
from immigration_forum.views import HomeView, CountryView, AddPostView, BlogView, EditPostView, ShowPostView, \
    DeletePostView, AddCommentView, like_post_view

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('country/<int:pk>/', CountryView.as_view(), name='country_details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('post/<int:pk>/edit_post/', EditPostView.as_view(), name='edit_post'),
    path('post/<int:pk>/', ShowPostView.as_view(), name='show_post'),
    path('post/<int:pk>/delete_post/', DeletePostView.as_view(), name='delete_post'),
    path('post/<int:pk>/add_comment/', AddCommentView.as_view(), name='add_comment'),
    path('post/<int:pk>/like/', like_post_view, name='like_post'),
]
