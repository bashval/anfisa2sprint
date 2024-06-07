from django.contrib import admin

from .models import Category, Topping, Wrapper, IceCream
from homepage.models import TestModel


admin.site.register(Category)
admin.site.register(Topping)
admin.site.register(Wrapper)
admin.site.register(TestModel)
admin.site.register(IceCream)