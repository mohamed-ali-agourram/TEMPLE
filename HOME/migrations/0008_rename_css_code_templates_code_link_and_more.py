# Generated by Django 4.0.5 on 2022-07-27 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0007_rename_code_link_templates_css_code_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='templates',
            old_name='css_code',
            new_name='code_link',
        ),
        migrations.RemoveField(
            model_name='templates',
            name='html_code',
        ),
        migrations.RemoveField(
            model_name='templates',
            name='js_code',
        ),
        migrations.AddField(
            model_name='templates',
            name='full',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]
