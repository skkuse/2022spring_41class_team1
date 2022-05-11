from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100, verbose_name='사용자명')
    password = models.CharField(max_length=100, verbose_name='비밀번호')

    #register_dttm = models.DataField(auto_now_add=True, verbose_name='가입날짜')

    def __str__(self):
        return self.username