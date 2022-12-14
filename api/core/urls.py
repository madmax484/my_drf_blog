
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, TagDetailView, TagView, AsideView, FeedBackView, RegisterView, ProfileView, CommentView, \
    UserPostRelationView

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register(r'posts_relations', UserPostRelationView)




urlpatterns = [
    path("", include(router.urls)),
    path("tags/", TagView.as_view()),
    path("tags/<slug:tag_slug>/", TagDetailView.as_view()),
    path("aside/", AsideView.as_view()),
    path("feedback/", FeedBackView.as_view()),
    path('register/', RegisterView.as_view()),
    path('profile/', ProfileView.as_view()),
    path("comments/", CommentView.as_view()),
    path("comments/<slug:post_slug>/", CommentView.as_view()),

    path('__debug__/', include('debug_toolbar.urls')),
]
