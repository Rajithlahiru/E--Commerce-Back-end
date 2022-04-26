from itertools import product
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from.serializers import ProductSerializers

from store.models import Product


# Create your views here.
@api_view()
def product_list(request):
    return Response('ok')

@api_view()
def product_details(request, id):
    product = Product.objects.get(pk=id)
    serializer = ProductSerializers(product)
    return Response(serializer.data)