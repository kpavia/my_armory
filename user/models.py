from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=32, unique=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['email', 'username'],
                name = 'User model'
            )
        ]
    
    def __str__(self):
        return f'User: {self.username}, email: {self.email}'
