from django.contrib import admin
from .models import Address, Doctor, Product, Bio, People
# Register your models here.
admin.site.register(Address)
admin.site.register(Doctor)
admin.site.register(Product)
admin.site.register(Bio)
admin.site.register(People)