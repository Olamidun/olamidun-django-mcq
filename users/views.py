from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2 and len(password) > 6:
            user = User.objects.create_user(username=username, email=email)
            user.set_password(password)
            user.save()
            return redirect('users:login')
        elif password != password2:
            # messages.success(request, 'Please ensure your passwords are the same.')
            return redirect('users:register')
        elif len(password) <= 6:
            # messages.success(request, 'Passwords must have a minimum of 7 characters!')
            return redirect('users:register')
    else:
        return render(request, 'users/register.html')