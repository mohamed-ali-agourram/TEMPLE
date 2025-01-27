# Generated by Django 4.0.5 on 2022-07-02 19:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='temp_category',
            fields=[
                ('title', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='temp_tag',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='templates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('ytb_link', models.TextField(blank=True, null=True)),
                ('html', models.TextField()),
                ('css', models.TextField()),
                ('js', models.TextField()),
                ('tags', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('desktop_img', models.ImageField(default='default_template.jpg', upload_to='template_pics')),
                ('mobile_img', models.ImageField(default='default_template_mobile.jpg', upload_to='template_pics')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HOME.temp_category')),
            ],
        ),
    ]
