from django.db import models
from django.contrib.auth.models import User  # Correct import

class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True)
    
    def __str__(self):
        return self.user.username

class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField(null=True)  # Corrected from TextFields to TextField

    def __str__(self):
        return self.title

class Product(models.Model):
    category=models.ForeignKey(ProductCategory,on_delete=models.SET_NULL,null=True,related_name='category_product')
    vendor=models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=200)  # Corrected from Chaerfileld to CharField
    detail = models.TextField(null=True)  # Corrected from TextFields to TextField
    price = models.IntegerField()

    def __str__(self):
        return self.title
    
#customer Model
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.PositiveBigIntegerField()
    
    def __str__(self):
        return self.user.username
    
#order model




class Order(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_time=models.DateTimeField(auto_now=True)
    
   
    
class OrderItems(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product.title
    
    

#customer address
class CustomerAddress(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='cutomer_address')
    address = models.TextField()
    default_address=models.BooleanField(default=False)
    def __str__(self):
        return self.address
    
#productraring&review

        
class ProductRating(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='rating_customer')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_ratings')
    rating=models.IntegerField()
    reviews=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
         return f'{self.rating} - {self.reviews}'
    