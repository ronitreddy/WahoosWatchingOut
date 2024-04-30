# Generated by Django 4.2.10 on 2024-03-14 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nbhood_watch', '0008_remove_user_user_name_user_email_user_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='Anonymous User', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='Anon', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='Anon', max_length=100),
        ),
    ]