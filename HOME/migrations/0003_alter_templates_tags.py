# Generated by Django 4.0.5 on 2022-07-06 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0002_remove_templates_tags_templates_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templates',
            name='tags',
            field=models.ManyToManyField(blank=True, to='HOME.temp_tag'),
        ),
    ]
