from records.models import Product

class Product (models.Model):
    Product_name = models.CharField(max_length=50)
    Product_price =  models.CharField(max_length=10000)

    def __str__(self):
        return self.Product_name 
    
#To insert a new record into the Product Model
drug1= Product(Product_name="Amartem", Product_price="N1000")
Product.save()

#To get all records in the Product model
Product.objects.all()

#To filter products by their name
Product.objects.filter(Product_name='Vitamin C Syrup')
Product.objects.filter(Product_name='Lonart DS')
Product.objects.filter(Product_name='Camosunate')

#To get a single record from the table
a=Product.objects.filter(Product_name='Camosunate').filter(Product_price='N1200').last()
#to return product name
a.Product_name
#to return product price
a.Product_price

#To Change a product price
a.Product_price='N2000'
a.save()