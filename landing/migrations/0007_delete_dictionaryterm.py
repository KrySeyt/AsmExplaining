# Generated by Django 4.1.1 on 2022-10-11 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0006_delete_article_dictionaryterm_slug_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DictionaryTerm',
        ),
    ]
