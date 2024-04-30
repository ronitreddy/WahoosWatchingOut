# Generated by Django 4.2.10 on 2024-03-24 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nbhood_watch', '0018_merge_20240324_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='submission_summary',
            new_name='submission_desc',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='submission_text',
        ),
        migrations.AddField(
            model_name='submission',
            name='submission_title',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='submission',
            name='submission_visibility',
            field=models.CharField(choices=[('Public', 'Public'), ('Only to Admin', 'Only to Admin')], default='Public', max_length=20),
        ),
    ]
