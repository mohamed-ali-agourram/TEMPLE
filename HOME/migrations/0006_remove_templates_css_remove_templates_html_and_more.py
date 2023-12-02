# Generated by Django 4.0.5 on 2022-07-21 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0005_alter_templates_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='templates',
            name='css',
        ),
        migrations.RemoveField(
            model_name='templates',
            name='html',
        ),
        migrations.RemoveField(
            model_name='templates',
            name='js',
        ),
        migrations.AddField(
            model_name='templates',
            name='code_link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='templates',
            name='full',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]
