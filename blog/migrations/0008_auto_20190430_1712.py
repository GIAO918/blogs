# Generated by Django 2.1.4 on 2019-04-30 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190430_1434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create',
            new_name='created_time',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='create_time',
            new_name='created_time',
        ),
    ]
