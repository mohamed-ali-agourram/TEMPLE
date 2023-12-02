from django.contrib import admin
from .models import (
    templates,
    temp_category,
    temp_tag
    )

admin.site.register(templates)
admin.site.register(temp_category)
admin.site.register(temp_tag)