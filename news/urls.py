from django.urls import path
from .views import PostList, PostDeatil

urlpatterns =[
    path('', PostList.as_view()),
    path('<int:pk>', PostDeatil.as_view())
]

