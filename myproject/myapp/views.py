from django.shortcuts import render, redirect
from django.db import connection
from .forms import MyForm
from .models import Contact

def my_view(request):
    if not Contact._meta.db_table in connection.introspection.table_names():
        # If the Contact table does not exist, create it
        with connection.schema_editor() as schema_editor:
            schema_editor.create_model(Contact)

    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            Contact.objects.create(
                pizza_type=form.cleaned_data['pizza_type'],
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

    if request.method == 'POST' and 'cleanup' in request.POST:
        # Handle cleanup button click
        Contact.objects.all().delete()
        return redirect('display_data')  # Redirect to the display_data view after cleanup

    return render(request, 'myapp/display_data.html', {'contacts': contacts})