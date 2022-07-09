from rest_framework import serializers
from app_social.models import Cumment
from sorl.thumbnail import get_thumbnail

# serilaizer


class CummentSerializer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField()
    avatar = serializers.SerializerMethodField()
    user_fullname = serializers.SerializerMethodField()

    def get_reply(self, obj):
        return CummentSerializer(obj.cumments.filter(validation=True), many=True).data

    def get_avatar(self, obj):
        im = get_thumbnail(obj.user.profile.avatar, '65x65', crop='center', quality=99)
        return im.url

    def get_user_fullname(self, obj):
        return obj.user.get_full_name() if obj.user.get_full_name() else obj.user.username

    class Meta:
        model = Cumment  # model
        exclude = ('content_type', 'validation', 'object_id',)
