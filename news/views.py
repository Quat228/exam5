from rest_framework import generics, views
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from . import models
from . import serializers
from . import permissions
from . import paginations


class NewsListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer
    permission_classes = [permissions.IsAuthorOrReadOnly, ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', ]
    ordering_fields = ['created', ]
    pagination_class = paginations.NewsNumberPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)


class NewsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer
    permission_classes = [permissions.IsAuthorOrReadOnly, ]


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthorOrReadOnly, ]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return super().get_queryset().filter(news_id=self.kwargs['news_id'])

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author, news_id=self.kwargs['news_id'])


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthorOrReadOnly, ]

    def get_queryset(self):
        return super().get_queryset().filter(news_id=self.kwargs['news_id'])


class StatusListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    permission_classes = [permissions.IsAdmin]


class StatusRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    permission_classes = [permissions.IsAdmin, ]


class NewsStatusCreateAPIView(views.APIView):
    permission_classes = [permissions.IsAuthor, ]

    def get(self, request, *args, **kwargs):
        status = models.Status.objects.filter(slug=self.kwargs['slug']).first()
        if status:
            try:
                models.NewsStatus.objects.create(
                    author=self.request.user.author,
                    news_id=self.kwargs['news_id'],
                    status=models.Status.objects.filter(slug=self.kwargs['slug']).first()
                )
                return Response('Status added', status=201)
            except Exception as e:
                return Response(f'You already added status', status=400)
        else:
            return Response('This status does not exist!', status=400)


class CommentStatusCreateAPIView(views.APIView):
    permission_classes = [permissions.IsAuthor, ]

    def get(self, request, *args, **kwargs):
        status = models.Status.objects.filter(slug=self.kwargs['slug']).first()
        if status:
            try:
                models.CommentStatus.objects.create(
                    author=self.request.user.author,
                    comment_id=self.kwargs['comment_id'],
                    status=models.Status.objects.filter(slug=self.kwargs['slug']).first()
                )
                return Response('Status added', status=201)
            except Exception as e:
                return Response(f'You already added status', status=400)
        else:
            return Response('This status does not exist!', status=400)





