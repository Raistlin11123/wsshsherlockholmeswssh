# Generated by Django 2.2 on 2019-06-01 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investigation1', '0007_auto_20190601_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clue',
            name='url_content',
            field=models.CharField(max_length=42, null=True, verbose_name='url_content'),
        ),
    ]
