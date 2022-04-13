from django.contrib import admin
from ncmsapp.models import bill
from ncmsapp.models import branch
from ncmsapp.models import card
from ncmsapp.models import customer
from ncmsapp.models import employee
from ncmsapp.models import item
from ncmsapp.models import order_placed

# Register your models here.
admin.site.register(bill)
admin.site.register(branch)
admin.site.register(card)
admin.site.register(customer)
admin.site.register(employee)
admin.site.register(item)
admin.site.register(order_placed)