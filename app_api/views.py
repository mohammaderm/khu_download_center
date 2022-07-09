from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.conf import settings
from rest_framework import status
from app_software.models import Software, Blogsoft
from app_book.models import Book, Blogbook
from app_social.models import Cumment
from app_api.serializer import CummentSerializer
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q


@api_view(['POST'])
@login_required
def like(request):
    obj_id = request.POST.get('id')
    obj_type = request.POST.get('type')
    if obj_type and obj_id:
        if obj_type in settings.ALLOWED_OBJECTS_TYPES:
            model = eval(obj_type)
            my_obj = model.objects.get(id=obj_id)
            if my_obj.likes.filter(user=request.user):
                my_obj.likes.filter(user=request.user).delete()
                if my_obj.counterlike != 0:
                    my_obj.counterlike -= 1
                    my_obj.save()
                return Response({"message": "دیس لایک شد"}, status=status.HTTP_200_OK)
            else:
                my_obj.likes.create(user=request.user)
                my_obj.counterlike += 1
                my_obj.save()
                return Response({"message": "لایک شد"}, status=status.HTTP_200_OK)
    return Response({"message": "اوه یه مشکلی پیش اومده"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@login_required
def bookmark(request):
    obj_id = request.POST.get('id')
    obj_type = request.POST.get('type')
    if obj_type and obj_id:
        if obj_type in settings.ALLOWED_OBJECTS_TYPES:
            model = eval(obj_type)
            my_obj = model.objects.get(id=obj_id)
            if my_obj.bookmarks.filter(user=request.user):
                my_obj.bookmarks.filter(user=request.user).delete()
                return Response({"message": "نشان برداشته شد"}, status=status.HTTP_200_OK)
            else:
                my_obj.bookmarks.create(user=request.user)
                return Response({"message": "نشان شد"}, status=status.HTTP_200_OK)
    return Response({"message": "اوه یه مشکلی پیش اومده"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def cumment(request):
    if not request.user.is_authenticated:
        return Response({"message": "برای نظر دادن ابتدا باید در سایت ثبت نام کنید."},
                        status=status.HTTP_200_OK)
    cumment = request.POST.get('value')
    if not cumment:
        return Response({"message": "ابتدا نظر خود را وارد کنید"},
                        status=status.HTTP_200_OK)
    obj_id = request.POST.get('id')
    obj_type = request.POST.get('type')
    if cumment and obj_type and obj_id:
        if obj_type in settings.ALLOWED_OBJECTS_TYPES:
            model = eval(obj_type)
            my_obj = model.objects.get(id=obj_id)
            my_obj.cumments.create(user=request.user, value=cumment)
            return Response({"message": "نظر شما پس از تایید نمایش داده میشود"}, status=status.HTTP_200_OK)
    return Response({"message": "اوه یه مشکلی پیش اومده"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def cummentdisplay(request):
    # import time
    # time.sleep(2)
    obj_id = request.GET.get('id')
    obj_type = obj_type = request.GET.get('type')
    if obj_id and obj_id.isdigit() and obj_type and obj_type in settings.ALLOWED_OBJECTS_TYPES:
        model = eval(obj_type)
        try:
            obj = model.objects.get(id=obj_id)
        except model.DoseNotExist:
            return Response({"message": "اوه یه مشکلی پیش اومده"}, status=status.HTTP_400_BAD_REQUEST)
        com = Cumment.objects.first()
        ct = ContentType.objects.get_for_model(com)
        cumments = obj.cumments.filter(Q(validation=True) & ~Q(content_type=ct))
        serializer = CummentSerializer(cumments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"message": "اوه یه مشکلی پیش اومده"}, status=status.HTTP_400_BAD_REQUEST)
