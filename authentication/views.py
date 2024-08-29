from django.shortcuts import render,redirect
from .models import TblUsers
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = TblUsers.objects.get(u_email=email)
        except TblUsers.DoesNotExist:
            print("DoesNotExist")
            return render(request, 'authentication/login.html', {'error': 'Invalid email or password'})
        
        if check_password(password, user.u_password):
            request.session['user_id'] = user.u_id
            return redirect('add_expenses')
        else:
            print('Invalid email or password')
            return render(request, 'authentication/login.html', {'error': 'Invalid email or password'})
    else:
        return render(request,'authentication/login.html')

# Create your views here.
def register(request):
    if request.method == "POST":
        if(request.POST['password'] == request.POST['confirmpassword']):
            new_user = TblUsers(u_email=request.POST['email'], u_password=make_password(request.POST['password']))
            new_user.save()
            return redirect('login')
        else:
            return render(request,'authentication/register.html')
    else:
        return render(request,'authentication/register.html')
    
def logout(request):
    request.session.flush()
    return redirect('login')