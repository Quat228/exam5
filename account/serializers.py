from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    password_2 = serializers.CharField(write_only=True)

    class Meta:
        model = models.User
        fields = ['username', 'password', 'password_2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['password_2']:
            raise serializers.ValidationError('Пароли не соотвестуют!')
        return data

    def create(self, validated_data):
        user = models.User(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()

        try:
            models.Author.objects.create(user=user)

        except Exception as e:
            user.delete()
            return f"Ошибка {e}"

        return user


