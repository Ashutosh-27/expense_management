from django.shortcuts import get_object_or_404, render,redirect

from authentication.models import TblUsers
from .models import TblExpenses,TblIncome,Category,Source
# Create your views here.
def index(request):
    return render(request,'expenses/index.html')

def add_expenses(request):
    if 'user_id' in request.session:
        if request.method == "POST":
            newexpense = TblExpenses(
                u_id= request.session['user_id'],
                amount=request.POST['amount'],
                category_id=request.POST['category'],
                datetime=request.POST['date'],
                description=request.POST['description'],
            )
            # print("Inside POST")
            newexpense.save()
            return redirect('expenses_summary')
        else:
            categories = Category.objects.filter(u_id= request.session['user_id'])
            return render(request,'expenses/add_expense.html',{"categories":categories})
    else:
        return redirect('login')

def edit_expenses(request):
    if 'user_id' in request.session:
        if request.method == "POST":
            expense = get_object_or_404(TblExpenses, pk=request.POST['expense'])
            expense.amount = request.POST['amount']
            expense.category_id = request.POST['category']
            expense.datetime = request.POST['date']
            expense.description = request.POST['description']
            expense.save()
        return redirect('expenses_summary')
    else:
        return redirect('login')


def add_income(request):
    if 'user_id' in request.session:
        if request.method == "POST":
            newincome = TblIncome(
                u_id= request.session['user_id'],
                amount=request.POST['amount'],
                source_id=request.POST['source'],
                datetime=request.POST['date'],
                description=request.POST['description'],
            )
            newincome.save()
            return redirect('income_summary')
        else:
            sources = Source.objects.filter(u_id= request.session['user_id'])
            return render(request,'expenses/add_income.html',{"sources":sources})
    else:
        return redirect('login')
    
def edit_income(request):
    if 'user_id' in request.session:
        if request.method == "POST":
            income = get_object_or_404(TblIncome, pk=request.POST['income'])
            income.amount = request.POST['amount']
            income.source_id = request.POST['source']
            income.datetime = request.POST['date']
            income.description = request.POST['description']
            income.save()
        return redirect('income_summary')
    else:
        return redirect('login')

def expense_summary(request):
    if 'user_id' in request.session:
        expenses = TblExpenses.objects.raw(
            'SELECT te.*, c.name as category_name FROM expenses_tblexpenses as te '
            'LEFT JOIN expenses_category as c ON c.category_id = te.category_id '
            'WHERE te.u_id = %s '
            'ORDER BY te.created_at',
            [request.session['user_id']]
        )
        categories = Category.objects.filter(u_id= request.session['user_id'])
        # categories = expenses.values('category_id__name').annotate(total_amount=Sum('amount'))
        # dates = expenses.values('datetime__date').annotate(total_amount=Sum('amount'))

        # category_data = {item['category_id__name']: item['total_amount'] for item in categories}
        # date_data = {item['datetime__date']: item['total_amount'] for item in dates}

        category_data =[]
        date_data = []
        
        return render(request,'expenses/expenses_summary.html',{"expenses":expenses,'category_data': category_data,
        'date_data': date_data,'categories':categories})
    else:
        return redirect('login')

def income_summary(request):
    if 'user_id' in request.session:
        # incomes = TblIncome.objects.filter(u_id=request.session['user_id']).order_by('-created_at')
        incomes = TblIncome.objects.raw(
            'SELECT ti.*, s.name as source_name FROM expenses_tblincome as ti '
            'LEFT JOIN expenses_source as s ON s.source_id = ti.source_id '
            'WHERE ti.u_id = %s '
            'ORDER BY ti.created_at',
            [request.session['user_id']]
        )
        sources = Source.objects.filter(u_id= request.session['user_id'])
        return render(request,'expenses/income_summary.html',{"incomes":incomes,'sources':sources})
    else:
        return redirect('login')
    
def categorys_sources(request):
    if 'user_id' in request.session:
        categories = Category.objects.filter(u_id= request.session['user_id'])
        sources = Source.objects.filter(u_id= request.session['user_id'])
        return render(request,'expenses/categories_source.html',{"categories":categories,"sources":sources})
    else:
        return redirect('login')

def add_category(request):
    if 'user_id' in request.session:
        user_instance = TblUsers.objects.get(u_id= request.session['user_id'])
        newcategory = Category(u_id=user_instance,name=request.POST['category'])
        newcategory.save()
        return redirect('categorys_sources')
    else:
        return redirect('login')
    
def add_source(request):
    if 'user_id' in request.session:
        user_instance = TblUsers.objects.get(u_id= request.session['user_id'])
        newsource = Source(u_id= user_instance,name=request.POST['source'])
        newsource.save()
        return redirect('categorys_sources')
    else:
        return redirect('login')
    
def delete_category(request):
    if 'user_id' in request.session:
        # Retrieve the category object by its id
        category = get_object_or_404(Category, category_id=request.POST['cid'])
        # Delete the category
        category.delete()
        return redirect('categorys_sources')
    else:
        return redirect('login')
    
def delete_source(request):
    if 'user_id' in request.session:
         # Retrieve the category object by its id
        source = get_object_or_404(Source, source_id=request.POST['sid'])
        # Delete the category
        source.delete()
        return redirect('categorys_sources')
    else:
        return redirect('login')
    
def delete_expense(request, e_id):
    expense = get_object_or_404(TblExpenses, pk=e_id)
    expense.delete()
    return redirect('expenses_summary') 

def delete_income(request, i_id):
    income = get_object_or_404(TblIncome, pk=i_id)
    income.delete()
    return redirect('income_summary') 