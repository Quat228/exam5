from django.db import models
from django.contrib.auth.models import AbstractUser


# В дальнейшем можно
class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='author')
    registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.registered}'
