from pyexpat import model
from django.db import models
from django.utils.translation import gettext as _
from category.models import Category
from django.urls import reverse
from django.core.validators import RegexValidator


class Product(models.Model):
    product_name_in_inglish    = models.CharField(_("اسم المنتج بالانجليزي"), max_length=200, unique=True, blank=True, null=True)
    product_name_in_arabic   = models.CharField(_("اسم المنتج بالعربي"),max_length=200, unique=True, blank=True, null=True)
    slug            = models.SlugField(_("اسم المنتج في الرابط"), max_length=200, unique=True)
    description     = models.TextField(_("الوصف بالإنجليزي"),  blank=True,null=True)
    descriptionin_arabic     = models.TextField(_(" الوصف بالعربي"),  blank=True, null=True)
    price           = models.CharField(_("السعر"), max_length=245,blank=True,default=0)
    is_price           = models.BooleanField(_("إظهار السعر؟"), default=False)
    images          = models.ImageField(_("الصوره") )
    is_available    = models.BooleanField(_("متوفر؟"),default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(_("تاريخ الأضافه"),auto_now_add=True)
    modified_date   = models.DateTimeField(_("اخر تعديل"),auto_now=True)


    class Meta:
        verbose_name = _("المنتج")
        verbose_name_plural = _("المنتجات")
    def get_url(self):
        return reverse('product_detail', args=[self.category.master_category.slug, self.category.slug, self.slug])

    def __str__(self):
        return self.is_price


class ProductImage(models.Model):
    images          = models.ImageField(_("الصوره") )
    product        = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    created_date    = models.DateTimeField(_("تاريخ الأضافه"),auto_now_add=True)
    modified_date   = models.DateTimeField(_("اخر تعديل"),auto_now=True)


    class Meta:
        verbose_name = _("صورة المنتج")
        verbose_name_plural = _("صور المنتجات")

    def __str__(self):
        return self.product.product_name_in_arabic


class CustomerRequests(models.Model):
    full_name = models.CharField(_("الأسم كامل"), max_length=250)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(_("رقم الموبيل") ,validators=[phone_regex], max_length=17) # validators should be a list
    email = models.EmailField(_("البريد"))
    note = models.TextField(_("ملحوظه"), null=True, blank=True)
    created_at = models.DateTimeField(_("تاريخ الأضافه"),auto_now_add=True)

    class Meta:
        verbose_name = _("طلب العميل")
        verbose_name_plural = _("طلبات العميل")


    def __str__(self):
        return self.full_name

class HomeReviews(models.Model):
    full_name = models.CharField(_("اسم"), max_length=200)
    department = models.CharField(_("وصف الشخص عميل او موظف"), max_length=200)
    description = models.TextField(_("الوصف"))

    class Meta:
        verbose_name = _("ريفيوا")
        verbose_name_plural = _("ريفيوهات عملاء")


    def __str__(self):
        return self.full_name


