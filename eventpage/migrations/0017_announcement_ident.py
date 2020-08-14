# Generated by Django 2.2.15 on 2020-08-14 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventpage', '0016_announcement_hide'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='ident',
            field=models.CharField(default='', max_length=250, verbose_name='Identification (visible to admin only)'),
            preserve_default=False,
        ),
    ]