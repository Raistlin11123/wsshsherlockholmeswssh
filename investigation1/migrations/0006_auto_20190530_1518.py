# Generated by Django 2.2 on 2019-05-30 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investigation1', '0005_clue_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userclues',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
