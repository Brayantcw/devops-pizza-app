from django.shortcuts import render, redirect
from .forms import MyForm
from .models import Contact

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            return redirect('thanks')
    else:
        form = MyForm()

    return render(request, 'myapp/form.html', {'form': form})

def thanks_view(request):
    return render(request, 'myapp/thanks.html')

def display_data_view(request):
    contacts = Contact.objects.all()
    return render(request, 'myapp/display_data.html', {'contacts': contacts})