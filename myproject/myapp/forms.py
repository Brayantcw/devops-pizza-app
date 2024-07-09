from django import forms

class MyForm(forms.Form):

    PIZZA_TYPES = [
        ('Margherita', 'Margherita'),
        ('Pepperoni', 'Pepperoni'),
        ('Vegetarian', 'Vegetarian')
    ]

    pizza_type = forms.ChoiceField(choices=PIZZA_TYPES, label='Pizza Types', initial='Pepperoni')
    message = forms.CharField(widget=forms.Textarea, label='Your message')
