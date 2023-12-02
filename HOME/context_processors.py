from .models import(
    templates,
    temp_category,
    temp_tag
)


def add_variable_to_context(request):
    categories = temp_category.objects.all()
    tags = temp_tag.objects.all()
    favorite = templates.objects.filter(tags__name__icontains="favorite")
    random1 = templates.objects.filter(id=45)
    random2 = templates.objects.filter(id=47)
    populer = templates.objects.all()[:3]
    return {
        'categories': categories,
        'tags' : tags,
        'favorite' : favorite,
        'random1' : random1,
        'random2' : random2,
        'populer' : populer
    }
