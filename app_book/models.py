from django.db import models
from django.contrib.auth.models import User
from app_social.models import Cumment, Like, Bookmark
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


def image_path(instance, filename):
    return "books-image/%s/%s" % (instance.title, filename)

def imageblog_path(instance, filename):
    return "books-image/blog/%s/%s" % (instance.title, filename)


def file_path(instance, filename):
    return "books-image/%s/%s" % (instance.book.title, filename)


class Category(models.Model):
    title = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=100, null=True, allow_unicode=True, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

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


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to=image_path, null=True)
    publish = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(max_length=100, null=True, allow_unicode=True, blank=True)
    cumments = GenericRelation(Cumment)
    likes = GenericRelation(Like)
    request_status = models.BooleanField(default=False)
    sugest = models.BooleanField(default=False)
    poster_sugest = models.ImageField(upload_to=image_path, null=True, blank=True)
    adminresult = models.TextField(null=True, blank=True)
    counterlike = models.PositiveIntegerField(default=0, null=True, blank=True)
    countercomment = models.PositiveIntegerField(default=0, null=True, blank=True)
    bookmarks = GenericRelation(Bookmark)
    counter_download = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(' ', '-') + str(self.id)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        params = {'slug': self.slug}
        return reverse("app_software:bookdetails", kwargs=params)

    def get_cat_list(self):
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb) - 1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i - 1:-1])
        return breadcrumb[-1:0:-1]


class Files(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    title_link = models.CharField(max_length=100, null=True, default='لینک دانلود')
    file = models.FileField(upload_to=file_path, null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, allow_unicode=True, blank=True)

    def __str__(self):
        return self.book.title

    def save(self, *args, **kwargs):
        self.slug = self.book.title.replace(' ', '-')
        super().save(*args, **kwargs)


class Blogbook(models.Model):
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
        return reverse("app_book:blogdetails", kwargs=params)
