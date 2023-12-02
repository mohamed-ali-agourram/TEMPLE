# Generated by Django 4.0.5 on 2022-07-27 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0006_remove_templates_css_remove_templates_html_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='templates',
            old_name='code_link',
            new_name='css_code',
        ),
        migrations.RemoveField(
            model_name='templates',
            name='full',
        ),
        migrations.AddField(
            model_name='templates',
            name='html_code',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='templates',
            name='js_code',
            field=models.TextField(blank=True, null=True),
        ),
    ]