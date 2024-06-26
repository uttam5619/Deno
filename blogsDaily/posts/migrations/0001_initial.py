# Generated by Django 5.0.4 on 2024-05-08 07:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='title', max_length=250)),
                ('descriptions', models.CharField(blank=True, default='description', max_length=500)),
                ('url', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='category/')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('postId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('subject', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('descriptions', models.TextField()),
                ('url', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='post/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.category')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentId', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=500)),
                ('commented_at', models.DateTimeField(auto_now_add=True)),
                ('commented_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
    ]
