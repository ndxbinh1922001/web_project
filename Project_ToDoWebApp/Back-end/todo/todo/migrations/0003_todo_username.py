# Generated by Django 3.2.8 on 2021-10-30 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='username',
            field=models.CharField(default='binh', max_length=100),
        ),
    ]