# Generated by Django 5.0.1 on 2024-05-16 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_post_category_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=100, null=True, verbose_name='Slug'),
        ),
    ]