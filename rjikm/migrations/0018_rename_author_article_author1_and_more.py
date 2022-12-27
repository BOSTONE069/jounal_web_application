# Generated by Django 4.0.1 on 2022-12-26 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rjikm', '0017_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author',
            new_name='author1',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='university',
            new_name='department1',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='email',
            new_name='email1',
        ),
        migrations.AddField(
            model_name='article',
            name='author2',
            field=models.CharField(default='Anonymous', max_length=100),
        ),
        migrations.AddField(
            model_name='article',
            name='department2',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='article',
            name='email2',
            field=models.EmailField(default='anonymous@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='article',
            name='university1',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='article',
            name='university2',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]