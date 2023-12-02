from django.db import models
from django.utils import timezone


class temp_category(models.Model):
    title = models.CharField(max_length=20, primary_key=True, unique=True)

    def __str__(self):
        return self.title


class temp_tag(models.Model):
    name = models.CharField(max_length=20, primary_key=True, unique=True)

    def __str__(self):
        return self.name


class templates(models.Model):
    title = models.CharField(max_length=100)
    ytb_link = models.TextField(null=True, blank=True)
    html_head = models.TextField(null=True, blank=True)
    html_body = models.TextField(null=True, blank=True)
    css_code = models.TextField(null=True, blank=True)
    js_code = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        temp_category, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(temp_tag, blank=True)
    description = models.TextField(null=True, blank=True)
    mobile_view = models.CharField(max_length=4, blank=True)
    desktop_img = models.ImageField(
        default='default_template.jpg', upload_to='template_pics')
    mobile_img = models.ImageField(
        default='default_template_mobile.jpg', upload_to='template_pics')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
