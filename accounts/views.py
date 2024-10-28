from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm  # Use the custom form


def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display a blank registration form.
        form = CustomUserCreationForm()  # Use the custom form
    else:
        # Process the completed form.
        form = CustomUserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to the home page.
            login(request, new_user)
            return redirect('onesimus_app:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)
