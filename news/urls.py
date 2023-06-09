from django.urls import path, include

from . import views


urlpatterns = [
    path('news/', views.NewsListCreateAPIView.as_view()),
    path('news/<int:pk>/', views.NewsRetrieveUpdateDestroyAPIView.as_view()),
    path('news/<int:news_id>/comments/', views.CommentListCreateAPIView.as_view()),
    path('news/<int:news_id>/comments/<int:pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view()),
    path('news/<int:news_id>/<str:slug>/', views.NewsStatusCreateAPIView.as_view()),
    path('news/<int:news_id>/comments/<int:comment_id>/<str:slug>/', views.CommentStatusCreateAPIView.as_view()),

    path('statuses/', views.StatusListCreateAPIView.as_view()),
    path('statuses/<int:pk>', views.StatusRetrieveUpdateDestroyAPIView.as_view()),
]
