# Generated by Django 5.0.7 on 2024-07-22 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_remove_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
