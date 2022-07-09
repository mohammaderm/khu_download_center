from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from app_social.models import Cumment, Like, Bookmark
from django.contrib.contenttypes.fields import GenericRelation


# Create your models here.


def file_path(instance, filename):
    return "%s/%s" % (instance.slug, filename)


def image_path(instance, filename):
    return "%s/%s" % (instance.slug, filename)


def imageblog_path(instance, filename):
    return "books-image/blog/%s/%s" % (instance.title, filename)


class Category(models.Model):
    title = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=100, null=True, allow_unicode=True, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(' ', '-')
        super().save(*args, **kwargs)

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])


class Software(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=True)
    description = RichTextUploadingField(null=True)
    version = models.CharField(max_length=100, null=True)
    system_requirment = RichTextUploadingField(null=True)
    tutorial_install = RichTextUploadingField(null=True)
    image = models.ImageField(upload_to=image_path, null=True)
    counter_download = models.IntegerField(null=True)
    publish = models.DateTimeField(auto_now=True, null=True)
    updatedescription = models.CharField(max_length=500, null=True, blank=True,
                                         default='اطلاعات توسط ادمین ثبت نشده است.')
    slug = models.SlugField(max_length=100, null=True, allow_unicode=True, blank=True)
    suggest = models.BooleanField(default=False)
    cumments = GenericRelation(Cumment)
    likes = GenericRelation(Like)
    counterlike = models.PositiveIntegerField(default=0, null=True, blank=True)
    countercomment = models.PositiveIntegerField(default=0, null=True, blank=True)
    bookmarks = GenericRelation(Bookmark, related_query_name='book')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(' ', '-')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        params = {'slug': self.slug}
        return reverse("app_software:software1", kwargs=params)

    def get_cat_list(self):
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb) - 1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i - 1:-1])
        return breadcrumb[-1:0:-1]


class File_Software(models.Model):
    software = models.ForeignKey(Software, on_delete=models.CASCADE)
    title_link = models.CharField(max_length=100, null=True, default='لینک دانلود')
    os_name = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField(upload_to=file_path, null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, allow_unicode=True, blank=True)

    def __str__(self):
        return self.software.title

    def save(self, *args, **kwargs):
        self.slug = self.software.title.replace(' ', '-')
        super().save(*args, **kwargs)


class Blogsoft(models.Model):
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to=imageblog_path, null=True)
    description = RichTextUploadingField(null=True)
    publish = models.DateTimeField(auto_now_add=True, null=True)
    cumments = GenericRelation(Cumment)
    slug = models.SlugField(max_length=100, null=True, allow_unicode=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(' ', '-') + str(self.id)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        params = {'slug': self.slug}
        return reverse("app_software:blogsoftdetails", kwargs=params)
