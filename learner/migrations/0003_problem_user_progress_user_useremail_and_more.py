# Generated by Django 4.0.3 on 2022-05-15 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learner', '0002_alter_user_password_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('pnumber', models.IntegerField(primary_key=True, serialize=False)),
                ('context_path', models.CharField(max_length=2000, verbose_name='문제내용 경로')),
                ('input_path', models.CharField(max_length=2000, verbose_name='인풋데이터 경로')),
                ('output_path', models.CharField(max_length=2000, verbose_name='아웃풋데이터 경로')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='progress',
            field=models.IntegerField(default=0, verbose_name='학습진행도'),
        ),
        migrations.AddField(
            model_name='user',
            name='useremail',
            field=models.CharField(default='', max_length=100, verbose_name='사용자이메일'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, verbose_name='사용자이름'),
        ),
    ]
