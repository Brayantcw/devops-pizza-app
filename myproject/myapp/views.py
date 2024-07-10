"""
This module contains the view functions for the myapp application.
"""

from django.shortcuts import render, redirect
from django.db import connection
from .forms import MyForm
from .models import Order

def my_view(request):
    """
    Handle new orders and db objects
    """

    if not Order._meta.db_table in connection.introspection.table_names():
        # If the Contact table does not exist, create it
        with connection.schema_editor() as schema_editor:
            schema_editor.create_model(Order)

    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            Order.objects.create(
                pizza_type=form.cleaned_data['pizza_type'],
                message=form.cleaned_data['message']
            )
            return redirect('thanks')
    else:
        form = MyForm()

    return render(request, 'myapp/form.html', {'form': form})

def thanks_view(request):
    """
    Handle the message when a new order is created
    """
    return render(request, 'myapp/thanks.html')


def display_data_view(request):
    """
    Handle the list of orders using a tabular style
    """
    orders = Order.objects.all()

    if request.method == 'POST' and 'cleanup' in request.POST:
        # Handle cleanup button click
        Order.objects.all().delete()
        return redirect('display_data')  # Redirect to the display_data view after cleanup

    return render(request, 'myapp/display_data.html', {'orders': orders})
