# Generated by Django 4.0.6 on 2022-08-30 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_options_remove_todo_user_todo_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='is_active',
        ),
        migrations.AlterField(
            model_name='todo',
            name='is_complete',
            field=models.BooleanField(verbose_name='Отложено'),
        ),
    ]
