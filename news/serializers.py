from rest_framework import serializers

from django.db.utils import IntegrityError

from . import models


class NewsSerializer(serializers.ModelSerializer):
    statuses = serializers.ReadOnlyField(source='get_status')

    class Meta:
        model = models.News
        fields = '__all__'
        read_only_fields = ['author', ]


class CommentSerializer(serializers.ModelSerializer):
    statuses = serializers.ReadOnlyField(source='get_status')

    class Meta:
        model = models.Comment
        fields = '__all__'
        read_only_fields = ['author', 'news', 'statuses']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields = '__all__'
