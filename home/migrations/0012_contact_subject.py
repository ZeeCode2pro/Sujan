# Generated by Django 5.1.6 on 2025-02-26 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_honor_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default='', max_length=200),
        ),
    ]
