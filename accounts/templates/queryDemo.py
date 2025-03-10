# Import Django models and ORM utilities
from django.db import models
from accounts.models import Customer, Order, Product  # Import your models here

# (1) Returns all customers from the customer table
customers = Customer.objects.all()

# (2) Returns the first customer in the table
firstCustomer = Customer.objects.first()

# (3) Returns the last customer in the table
lastCustomer = Customer.objects.last()

# (4) Returns a single customer by name
customerByName = Customer.objects.get(name='Jitendra Joshi')

# (5) Returns a single customer by ID
customerById = Customer.objects.get(id=4)

# (6) Returns all orders related to the first customer (firstCustomer variable set above)
firstCustomerOrders = firstCustomer.order_set.all()

# (7) Returns the name of the customer for the first order (Query parent model values)
order = Order.objects.first()
parentName = order.customer.name

# (8) Returns products from the products table with the value "Out Door" in the category attribute
products = Product.objects.filter(category="Out Door")

# (9) Orders/Sorts products by ID
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')

# (10) Returns all products with the tag "Sports" (Query Many-to-Many Fields)
productsFiltered = Product.objects.filter(tags__name="Sports")

# (11) Bonus

# Q: If the customer has more than 1 ball, how would you reflect it in the database?

# A: Because there are many different products and this value changes constantly,
# you would most likely not want to store the value in the database but rather
# just make this a function we can run each time we load the customer's profile.

# Returns the total count of times a "Ball" was ordered by the first customer
ballOrders = firstCustomer.order_set.filter(product__name="Ball").count()

# Returns total count for each product ordered by the first customer
allOrders = {}
for order in firstCustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1

# Returns: allOrders = {'Ball': 2, 'BBQ Grill': 1}

# RELATED SET EXAMPLE
class ParentModel(models.Model):
    name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
# Returns all child models related to the parent
parentChildren = parent.childmodel_set.all()
