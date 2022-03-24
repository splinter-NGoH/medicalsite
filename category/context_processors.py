from .models import Category, MasterCategory

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)

def menu_links(request):
    masterlinks = MasterCategory.objects.all()
    return dict(masterlinks=masterlinks)