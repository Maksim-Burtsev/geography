# Generated by Django 4.0.3 on 2022-03-23 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-publish_time'], 'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AddField(
            model_name='topic',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='topic_photo', verbose_name='Фото'),
        ),
    ]
