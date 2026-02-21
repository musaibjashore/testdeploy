from django.urls import path
from .views import homepage,postview,newpost,editpost,deletepost,CommentView,ProfileView

urlpatterns=[
    path('profile/<int:pk>/', ProfileView.as_view(),name='profile'),
    path('post/<int:pk>/delete/', deletepost.as_view(),name='post_delete'),
    path('post/<int:pk>/edit/',editpost.as_view(),name='post_edit'),
    path('post/new/',newpost.as_view(),name='post_new'),
    path('',homepage.as_view(), name='home'),
    path('post/<int:pk>/',postview.as_view(),name='post'),
    path('post/<int:pk>/comment',CommentView.as_view(),name='comment'),
    ]
