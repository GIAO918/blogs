# Generated by Django 2.1.4 on 2019-04-30 06:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190430_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='owner',
            field=models.ForeignKey(on_delete=None, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=None, to='blog.Category', verbose_name='分类'),
        ),
        migrations.AlterField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(on_delete=None, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='owner',
            field=models.ForeignKey(on_delete=None, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
    ]
