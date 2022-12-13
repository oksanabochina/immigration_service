from django.urls import path, include
from rest_framework_nested import routers
from immigration_api.views import PostViewSet, CommentViewSet, ConsultantProfileViewSet, CountryViewSet, \
    UserProfileViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('consultantprofiles', ConsultantProfileViewSet)
router.register('userprofiles', UserProfileViewSet)
router.register('countries', CountryViewSet)

post_router = routers.NestedDefaultRouter(router, 'posts', lookup='post')
post_router.register('comments', CommentViewSet, basename='post-comment')

urlpatterns = router.urls + post_router.urls

