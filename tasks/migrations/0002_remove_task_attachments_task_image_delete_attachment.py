# Generated by Django 4.2.5 on 2023-10-24 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='attachments',
        ),
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_rgq6aq', upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='Attachment',
        ),
    ]
