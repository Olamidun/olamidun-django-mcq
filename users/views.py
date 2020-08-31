from django.shortcuts import render, redirect, HttpResponse
from .forms import UserRegistrationForm
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} you have successfully created an account, you are now able to login')
            return redirect('login')
        else:
            return HttpResponse('Invalid details')
    else:
        form = UserRegistrationForm()
        return render(request, 'users/register.html', {'form': form})