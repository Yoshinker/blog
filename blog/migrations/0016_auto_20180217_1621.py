# Generated by Django 2.0.2 on 2018-02-17 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_remove_article_jv'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='les_pour',
            new_name='les_plus',
        ),
    ]
