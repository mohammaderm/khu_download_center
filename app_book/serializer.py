from rest_framework import serializers
from app_book.models import *
from sorl.thumbnail import get_thumbnail


class pagination_ser(serializers.ModelSerializer):
    imagesoft = serializers.SerializerMethodField()
    catsoft = serializers.SerializerMethodField()
    subcat = serializers.SerializerMethodField()

    def get_imagesoft(self, obj):
        im = get_thumbnail(obj.image, '160x214', crop='center', quality=99)
        return im.url

    def get_catsoft(self, obj):
        return obj.category.title

    def get_subcat(self, obj):
        return obj.category.parent.title

    class Meta:
        model = Book
        exclude = ('image', 'counter_download',
                   'description')


class blogser(serializers.ModelSerializer):
    imagesoft = serializers.SerializerMethodField()

    def get_imagesoft(self, obj):
        im = get_thumbnail(obj.image, '350x173', crop='center', quality=99)
        return im.url

    class Meta:
        model = Blogbook
        exclude = ('title', 'description',
                   'publish', 'image')

class bookser(serializers.ModelSerializer):
    imagesoft = serializers.SerializerMethodField()

    def get_imagesoft(self, obj):
        im = get_thumbnail(obj.poster_sugest, '350x173', crop='center', quality=99)
        return im.url

    class Meta:
        model = Blogbook
        exclude = ('title', 'description',
                   'publish', 'image')
