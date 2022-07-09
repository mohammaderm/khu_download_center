from django import template
from app_social.models import Bookmark, Like

register = template.Library()



@register.filter
def is_liked(obj, user):
    return user.is_authenticated and obj.likes.filter(user=user)


@register.filter
def is_bookmarked(obj, user):
    return user.is_authenticated and obj.bookmarks.filter(user=user)