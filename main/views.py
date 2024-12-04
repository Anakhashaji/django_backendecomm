from django.shortcuts import render
from rest_framework import generics,permissions,pagination,viewsets
from .import serializers
from .import models
from .import serializers
# Create your views here.
class VendorList(generics.ListCreateAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class=serializers.VendorSerializer
    
class VendorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class=serializers.VendorDetailSerializer
    
class ProductList(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductListSerializer  
    pagination_class=pagination.LimitOffsetPagination
    
    def get_queryset(self):
        qs=super().get_queryset()
        category=self.request.GET['category']
        category=models.ProductCategory.objects.get(id=category)
        qs=qs.filter(category=category)
        return qs
        
    

   
class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Product.objects.all()
    serializer_class=serializers.ProductDetailSerializer
    
class CustomerList(generics.ListCreateAPIView):
    queryset=models.Customer.objects.all()
    serializer_class=serializers.CustomerSerializer
    
class CustomerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Customer.objects.all()
    serializer_class=serializers.CustomerDetailSerializer
    
    
class OrderList(generics.ListCreateAPIView):
    queryset=models.Order.objects.all()
    serializer_class=serializers.OrderSerializer
    
class OrderDetail(generics.ListCreateAPIView):
    #queryset=models.OrderItems.objects.all()
    serializer_class=serializers.OrderDetailSerializer
    
    def get_queryset(self):
        order_id=self.kwargs['pk']
        order=models.Order.objects.get(id=order_id)
        order_items=models.OrderItems.objects.filter(order=order)
        return order_items
  
class CustomerAddressViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.CustomerAddresserializer
    queryset=models.CustomerAddress.objects.all() 
    
  
class ProductRatingViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.ProductRatingSerializer
    queryset=models.ProductRating.objects.all() 
    
    
#caategorylist
class CategoryList(generics.ListCreateAPIView):
    queryset=models.ProductCategory.objects.all()
    serializer_class=serializers.CategorySerializer
    
class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.ProductCategory.objects.all()
    serializer_class=serializers.CategoryDetailSerializer