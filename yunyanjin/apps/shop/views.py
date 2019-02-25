from rest_framework import viewsets, mixins, generics
from .serializers import ProductDetailSerializer, ProductPhotoSerializer, ItemSerializer
from .models import Product, Photo, Item
from django_filters.rest_framework import DjangoFilterBackend
from utils.publicpagination import PublicPagination


class ProductDetailViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all().order_by('id')
    pagination_class = PublicPagination
    serializer_class = ProductDetailSerializer


class ProductPhotoViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Photo.objects.all()
    serializer_class = ProductPhotoSerializer
    pagination_class = PublicPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('product',)


class ProductItemViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = PublicPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('product',)
