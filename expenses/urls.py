from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index,name='dashboard'),
    path('addexpenses', views.add_expenses,name='add_expenses'),
    path('addincome', views.add_income,name='add_income'),
    path('expensesummary', views.expense_summary,name='expenses_summary'),
    path('incomesummary', views.income_summary,name='income_summary'),
    path('categoryssources', views.categorys_sources,name='categorys_sources'),
    path('addCategory', views.add_category,name='add_category'),
    path('addSource', views.add_source,name='add_source'),
    path('deleteCategory', views.delete_category, name='delete_category'),
    path('deleteSource', views.delete_source, name='delete_source'),
    path('editExpenses', views.edit_expenses, name='edit_expenses'),
    path('editIncome', views.edit_income, name='edit_income'),
    path('deleteExpense/<int:e_id>/', views.delete_expense, name='delete_expense'),
    path('deleteIncome/<int:i_id>/', views.delete_income, name='delete_income'),
]
