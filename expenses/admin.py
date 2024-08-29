from django.contrib import admin
from .models import TblExpenses,Category,Source,TblIncome
# Register your models here.
admin.site.register(TblExpenses)
admin.site.register(TblIncome)
admin.site.register(Category)
admin.site.register(Source)
