# Generated by Django 2.1.5 on 2019-01-20 03:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190120_0340'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2019, 1, 20, 3, 54, 15, 944140, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postmodel',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(default='New Title', max_length=30, unique=True, verbose_name='Post Title'),
        ),
    ]
