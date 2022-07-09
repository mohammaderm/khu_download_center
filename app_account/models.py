from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


def image_path(instance, filename):
    return "accounts_avatar/%s/%s" % (instance.user.username, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    avatar = models.ImageField(upload_to=image_path, default='default-avatar.jpg', null=True, blank=True)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    def __str__(self):
        return self.user.username


class Softrequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    softname = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    request_status = models.BooleanField(default=False)
    publish_date = models.DateTimeField(auto_now_add=True, null=True)
    adminresult = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.softname
