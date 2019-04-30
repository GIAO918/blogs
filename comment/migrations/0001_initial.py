# Generated by Django 2.1.4 on 2019-04-30 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0007_auto_20190430_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=2000, verbose_name='内容')),
                ('nickname', models.CharField(max_length=50, verbose_name='昵称')),
                ('website', models.URLField(verbose_name='网站')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除')], default=1, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('target', models.ForeignKey(on_delete=None, to='blog.Post', verbose_name='评论目标')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
    ]
