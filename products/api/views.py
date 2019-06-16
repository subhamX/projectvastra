from seller.models import Entrepreneur
from products import serializer as serial
from products import models
from rest_framework import viewsets

# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status


# class ProductList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = models.Product.objects.all()
#         snippets1 = models.Product.objects.all()
#         serializer = serial.ProductsSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = serial.ProductsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser

# def product_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = models.Product.objects.all()
#         serializer = serial.ProductsSerializer(snippets, context={ 'name1' : 'Subham'}, many=True)
#         return JsonResponse(serializer.data, safe=False)


# Create your views here.

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serial.ProductsSerializer

# @api_view(['GET', 'POST'])
# def ProductsViewSet(request):
#     if(request.method == 'GET'):
#         products = models.Product.objects.all()
#         serializer = serial.ProductsSerializer(products, many=True)
#         return Response(serializer.data)


    # queryset = models.Product.objects.all()
    # serializer_class = serial.ProductsSerializer

