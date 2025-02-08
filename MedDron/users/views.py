from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_not_required, login_required
from .models import UserData

# Create your views here.

@login_not_required
def Login(request):
    if request.user.is_authenticated:
            try:
            # Get the Employee profile related to the logged-in user
                employee_profile = UserData.objects.get(user=request.user)
                
                if employee_profile.role == UserData.MANAGER:
                    # Redirect to the manager page
                    return redirect('manager')  # Ensure this URL name is correct
                else:
                    # Redirect to the employee page
                    return redirect('employe')  # Ensure this URL name is correct
            except UserData.DoesNotExist:
                print("no profile")
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
        
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                try:
                    userRole = UserData.objects.get(user=user)
                    if userRole.role == UserData.MANAGER:
                        return redirect('manager')  # Redirect to the manager's page
                    else:
                        return redirect('employe')  # Redirect to the employee's page
                except UserData.DoesNotExist:
                    print('none')            
            else:
                print("yo")
                messages.error(request, 'Username or Password is incorrect')
                return render(request, 'login.html')
            
    return render(request, 'login.html')


def logout_view(request):
    logout(request) 
    return redirect('login')  

@login_required
def manager_view(request):
    employees = UserData.objects.filter(role=UserData.EMPLOYEE)
    return render(request, 'Manager.html', {'employees': employees})

@login_required
def employe_view(request):
    return render(request, 'Employe.html')

def home(request):
    return render(request, 'home.html')