# Generated by Django 2.2.4 on 2019-09-20 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_auther'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='auther',
            new_name='author',
        ),
    ]