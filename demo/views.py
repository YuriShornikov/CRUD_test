from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from demo.models import Comment
from demo.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user',]# в get запросе используем для фильтрации /?user=
    search_fields = ['text']# в get запросе используем для фильтрации /?search=
    ordering_fields = ['id', 'text', 'create_at',]# в get запросе используем для фильтрации ?ordering= , так же "-" фильтрует в обратном порядке
    pagination_class = LimitOffsetPagination# ?limit= и дополнительно через &offset=