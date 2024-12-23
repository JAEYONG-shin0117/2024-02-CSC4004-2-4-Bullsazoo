from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    personal_id = models.CharField(max_length=100, unique=True)  # 개인식별 ID

    USERNAME_FIELD = 'username'  # 사용자 이름이 ID로 사용됨
    REQUIRED_FIELDS = []  # 추가 필드는 필요하지 않음 (personal_id는 비밀번호로 처리됨)

    def __str__(self):
        return self.username
