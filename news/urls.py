from django.urls import path
from .views import PostList, PostDetail, PostSearch, CreatePostView, DeletePostView, UpdatePostView
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path('', PostList.as_view(), name='posts'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search', PostSearch.as_view()),
    path('add', CreatePostView.as_view(), name='post_create'),
    path('<int:pk>/edit/', UpdatePostView.as_view(), name='post_update'),
    path('<int:pk>/delete/', DeletePostView.as_view(), name='post_delete'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]

