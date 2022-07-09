from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app_software.models import Software, File_Software, Category, Blogsoft
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from app_software.serializer import *
from rest_framework import filters
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status


def home(request):
    ctx = {}
    ctx['asd'] = Software.objects.all()
    ctx['lastupdatea'] = Software.objects.all().order_by('-publish')
    return render(request, 'index.html', ctx)


class Pagination_pro(ListAPIView):
    queryset = Software.objects.all()
    serializer_class = pagination_ser
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_fields = ['category', 'suggest']


def software2(request, slug):
    ctx = {}
    ctx['software3'] = ctxs = Software.objects.get(slug=slug)
    ctx['software8'] = ctxs.file_software_set.all()
    ctx['software4'] = Software.objects.all().order_by('-publish').exclude(slug=slug)
    return render(request, 'soft_detail.html', ctx)


@api_view(['GET'])
def mostlike(request):
    obj_type = obj_type = request.GET.get('type')
    if obj_type and obj_type in settings.ALLOWED_OBJECTS_TYPES:
        model = eval(obj_type)
        try:
            obj = model.objects.order_by('-counterlike')[:10]
        except model.DoseNotExist:
            return Response({"message": "اوه یه مشکلی پیش اومده"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = mostlikes(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"message": "اوه یه مشکلی پیش اومده"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def mostcomment(request):
    obj_type = obj_type = request.GET.get('type')
    if obj_type and obj_type in settings.ALLOWED_OBJECTS_TYPES:
        model = eval(obj_type)
        try:
            obj = model.objects.order_by('-countercomment')[:10]
        except model.DoseNotExist:
            return Response({"message": "اوه یه مشکلی پیش اومده"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = mostlikes(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"message": "اوه یه مشکلی پیش اومده"}, status=status.HTTP_400_BAD_REQUEST)


def blogsoftdetails(request, slug):
    ctx = {}
    ctx['blogdets'] = Blogsoft.objects.get(slug=slug)
    return render(request, 'blogsoft_details.html', ctx)


@api_view(['GET'])
def blogsoftpost(request):
    obj_type = request.GET.get('type')
    if obj_type and obj_type in settings.ALLOWED_OBJECTS_TYPES:
        model = eval(obj_type)
        try:
            obj = model.objects.all()
        except model.DoseNotExist:
            return Response({"message": "اوه یه مشکلی پیش اومده"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = blogser(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"message": "اوه یه مشکلی پیش اومده"}, status=status.HTTP_400_BAD_REQUEST)
