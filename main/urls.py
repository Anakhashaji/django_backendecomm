from django.urls import path,include
from .import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register('address',views.CustomerAddressViewSet)
router.register('productrating',views.ProductRatingViewSet)

urlpatterns = [
   
    path("vendors",views.VendorList.as_view()),
    path("vendor/<int:pk>/",views.VendorDetails.as_view()),
    #product
    path('products/',views.ProductList.as_view()),
    path('product/<int:pk>/',views.ProductDetails.as_view()),
    
      #productcategory
    path('categories/',views. CategoryList.as_view()),
    path('category/<int:pk>/',views.CategoryDetails.as_view()),
    
    #customers
    path("customers/",views.CustomerList.as_view()),
    path("customer/<int:pk>/",views.CustomerDetails.as_view()),
    
    #orders
    path("orders/",views.OrderList.as_view()),
    path("order/<int:pk>/",views.OrderDetail.as_view()),
]

# Include the router URLs
urlpatterns += router.urls