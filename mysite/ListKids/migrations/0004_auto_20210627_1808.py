# Generated by Django 3.0.14 on 2021-06-27 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ListKids', '0003_post_kids_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_kids',
            name='img',
            field=models.ImageField(blank=True, upload_to='admin/%Y/%m/%d/'),
        ),
    ]
