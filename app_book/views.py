from django.shortcuts import render
from app_book.models import Book, Category, Blogbook
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app_book.serializer import pagination_ser, blogser, bookser
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.


def bookhome(request):
    ctx = {}
    ctx['sub'] = Category.objects.filter(parent__isnull=True)
    ctx['lastupdatea'] = Book.objects.all().order_by('-publish')
    return render(request, 'book.html', ctx)


def bookdetails(request, slug):
    ctx = {}
    ctx['book3'] = ctxs = Book.objects.get(slug=slug)
    ctx['book8'] = ctxs.files_set.all()
    return render(request, 'book_detail.html', ctx)


def blogbookdetails(request, slug):
    ctx = {}
    ctx['blogdet'] = Blogbook.objects.get(slug=slug)
    return render(request, 'blog_details.html', ctx)


@api_view(['GET'])
def blogpost(request):
    obj_type = request.GET.get('type')
    if obj_type and obj_type in settings.ALLOWED_OBJECTS_TYPES:
        model = eval(obj_type)
        try:
            obj = model.objects.all()[:3]
        except model.DoseNotExist:
            return Response({"message": "اوه یه مشکلی پیش اومده"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = blogser(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"message": "اوه یه مشکلی پیش اومده"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def bookpost(request):
    obj_type = request.GET.get('type')
    if obj_type and obj_type in settings.ALLOWED_OBJECTS_TYPES:
        model = eval(obj_type)
        try:
            obj = model.objects.filter(sugest=True)[:3]
        except model.DoseNotExist:
            return Response({"message": "اوه یه مشکلی پیش اومده"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = bookser(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"message": "اوه یه مشکلی پیش اومده"}, status=status.HTTP_400_BAD_REQUEST)


class ExamplePaginations(PageNumberPagination):
    page_size = 12


class ExamplePagination(PageNumberPagination):
    page_size = 7


class Pagination(ListAPIView):
    queryset = Book.objects.filter(request_status=True)
    serializer_class = pagination_ser
    pagination_class = ExamplePaginations
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_fields = ['category']


class Mostlike(ListAPIView):
    queryset = Book.objects.filter(request_status=True).order_by('-counterlike')
    serializer_class = pagination_ser
    pagination_class = ExamplePagination


class Mostcom(ListAPIView):
    queryset = Book.objects.filter(request_status=True).order_by('-countercomment')
    serializer_class = pagination_ser
    pagination_class = ExamplePagination

class Store(ListAPIView):
    queryset = Book.objects.filter(request_status=True, category_id=37).order_by('-counterlike')
    serializer_class = pagination_ser
    pagination_class = ExamplePagination

class Storef(ListAPIView):
    queryset = Book.objects.filter(request_status=True, category_id=38).order_by('-counterlike')
    serializer_class = pagination_ser
    pagination_class = ExamplePagination
        
