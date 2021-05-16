from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

# Fired every time a request hits the 'signup/' URL
# Need to differentiate between POST and GET requests
def signup_view(request):
    if request.method == 'POST':
        # Sending data into the form for validation
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Log user in
            user = form.save()
            login(request, user)
            
            # Redirect user to articles URL named list (article homepage)
            return redirect('articles:list')
    
    else:
        form = UserCreationForm()
    
    # Send instance of form to the template
    return render(request, 'accounts/signup.html', { 'form': form })


def login_view(request):
    if request.method == 'POST':
        # Validation
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('articles:list')
    
    # If GET    
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', { 'form': form })

