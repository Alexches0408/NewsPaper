from django.urls import path
from .views import PostList, PostDetail, PostSearch, CreatePostView, DeletePostView, UpdatePostView

urlpatterns =[
    path('', PostList.as_view(), name='posts'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search', PostSearch.as_view()),
    path('add', CreatePostView.as_view(), name='post_create'),
    path('<int:pk>/edit/', UpdatePostView.as_view(), name='post_update'),
    path('<int:pk>/delete/', DeletePostView.as_view(), name='post_delete')
]

