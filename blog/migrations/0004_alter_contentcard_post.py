# Generated by Django 3.2.15 on 2022-10-14 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentcard',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contentcard', to='blog.post', verbose_name='紐づく記事'),
        ),
    ]
