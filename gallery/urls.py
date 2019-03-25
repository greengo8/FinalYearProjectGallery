from django.urls import path
from . views import GalleryPageView, CreatePostView

urlpatterns = [

    path('gallery-home/', GalleryPageView.as_view(), name='gallery-home'),
    path('gallery-post/', CreatePostView.as_view(), name='gallery-post'),

]
