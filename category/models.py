from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

class Category(models.Model):
    category_name_inenglish = models.CharField(_("اسم القسم بالانجليزي"), max_length=255, unique=True)
    category_name_inarabic = models.CharField(_("اسم القسم بالعربي"), max_length=255, unique=True)
    slug = models.SlugField(_("اسم القسم في الرابط"), max_length=100, unique=True)
    description = models.TextField(_("الوصف"), max_length=255, blank=True)
    cat_image = models.ImageField(_("صوره لو في"),  blank=True)


    class Meta:
        verbose_name = _('القسم')
        verbose_name_plural = _("الأقسام")

    def get_url(self):
            return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name_inarabic


class HomeSliedes(models.Model):
    title = models.CharField(_("العنوان"), max_length=250)
    description = models.TextField(_("الوصف"))
    slide_image = models.ImageField(_("صوره"))

    class Meta:
        verbose_name = _("الصفحة الرئيسية")
        verbose_name_plural = _("صور الصفحة الرئيسية")
    
    def __str__(self):
        return self.title