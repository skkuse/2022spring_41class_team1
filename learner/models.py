from django.db import models

# Create your models here.


class User(models.Model):
    useremail = models.CharField(max_length=100,default='', verbose_name='사용자이메일')
    password = models.CharField(max_length=100, verbose_name='비밀번호')
    
    username = models.CharField(max_length=100, verbose_name='사용자이름')
    progress = models.IntegerField(default = 0, verbose_name='학습진행도')

    #register_dttm = models.DataField(auto_now_add=True, verbose_name='가입날짜')

    def __str__(self):
        return self.useremail

class Problem(models.Model):
    pnumber = models.IntegerField(primary_key=True)
    context_path = models.CharField(max_length=2000, verbose_name='문제내용 경로')
    input_path = models.CharField(max_length=2000, verbose_name='인풋데이터 경로')
    output_path = models.CharField(max_length=2000, verbose_name='아웃풋데이터 경로')
    