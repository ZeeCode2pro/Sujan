# Generated by Django 5.1.6 on 2025-02-26 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_organization_involved_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='honor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/honor/'),
        ),
    ]
