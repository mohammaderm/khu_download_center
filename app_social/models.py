from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.content_object.title


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.content_object.title


class Cumment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    value = models.CharField(max_length=400, null=True)
    validation = models.BooleanField(default=False)
    publish_date = models.DateTimeField(auto_now_add=True, null=True)
    cumments = GenericRelation('Cumment')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        if hasattr(self.content_object, 'title'):
            return '%s-%s' % (self.content_object.title, ''.join(self.value.split()[:30]))
        else:
            return ''.join(self.value.split()[:30])


class Cummentlike(models.Model):
    LIKE_TYPES = (
        ('1', 'میپسندم'),
        ('-1', 'نمیپسندم'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cumment = models.ForeignKey(Cumment, on_delete=models.CASCADE, null=True)
    values = models.SmallIntegerField(null=True, choices=LIKE_TYPES)

    def __str__(self):
        return self.cumment.content_object.title
