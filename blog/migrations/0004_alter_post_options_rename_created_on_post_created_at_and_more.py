# Generated by Django 5.0.6 on 2024-05-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_updated_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='updated_on',
            new_name='updated_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='metades',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[(0, 'Draft'), (1, 'Publish'), (2, 'Delete')], default='draft', max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
