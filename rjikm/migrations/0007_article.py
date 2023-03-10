# Generated by Django 4.0.1 on 2022-12-22 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rjikm', '0006_editorinchief_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.CharField(default='untitled', max_length=100)),
                ('title', models.CharField(default='Untitled', max_length=100)),
                ('author', models.CharField(default='Anonymous', max_length=100)),
                ('university', models.CharField(default='Unknown', max_length=100)),
                ('email', models.EmailField(default='anonymous@example.com', max_length=254)),
                ('abstract', models.TextField(default='No abstract provided')),
                ('keywords', models.CharField(default='None', max_length=100)),
            ],
        ),
    ]
