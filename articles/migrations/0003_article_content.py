# Generated by Django 4.2.5 on 2023-09-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_remove_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default='nada'),
            preserve_default=False,
        ),
    ]
