from django.db import models

from authentication.models import TblUsers

# Create your models here.
class TblExpenses(models.Model):
    expense_id = models.AutoField(primary_key=True)
    u_id = models.IntegerField(max_length=10)  # Assumes you have a Category model
    amount = models.DecimalField(max_digits=10, decimal_places=2) 
    category_id = models.IntegerField(max_length=10)  # Assumes you have a Category model
    datetime = models.DateField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Expense {self.expense_id} - {self.amount}'
    
class TblIncome(models.Model):
    income_id = models.AutoField(primary_key=True)
    u_id = models.IntegerField(max_length=10)  # Assumes you have a Category model
    amount = models.DecimalField(max_digits=10, decimal_places=2) 
    source_id = models.IntegerField(max_length=10)  # Assumes you have a Category model
    datetime = models.DateField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Income {self.income_id} - {self.amount}'
    

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    u_id = models.ForeignKey(TblUsers, on_delete=models.CASCADE)

    def __str__(self):
        return f'Category {self.name} - {self.u_id}'
    
class Source(models.Model):
    source_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    u_id = models.ForeignKey(TblUsers, on_delete=models.CASCADE)

    def __str__(self):
        return f'Source {self.name} - {self.u_id}'
