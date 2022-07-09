
from rest_framework import serializers
from .models import *
from sorl.thumbnail import get_thumbnail


class pagination_ser(serializers.ModelSerializer):
    imagesoft = serializers.SerializerMethodField()
    catsoft = serializers.SerializerMethodField()

    def get_imagesoft(self, obj):
        im = get_thumbnail(obj.image, '213x132', crop='center', quality=99)
        return im.url

    def get_catsoft(self, obj):
        return obj.category.title

    class Meta:
        model = Software
        exclude = ('image', 'counter_download', 'tutorial_install',
                   'system_requirment', 'description')


class mostlikes(serializers.ModelSerializer):
    class Meta:
        model = Software
        exclude = ('image', 'counter_download', 'tutorial_install',
                   'system_requirment', 'description',
                   'version', 'publish', 'suggest', 'category')


class blogser(serializers.ModelSerializer):

    class Meta:
        model = Blogsoft
        exclude = ('description',
                   'publish', 'image')
