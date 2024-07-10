from django import forms

class MyForm(forms.Form):

    PIZZA_TYPES = [
        ('Margherita', 'Margherita'),
        ('Pepperoni', 'Pepperoni'),
        ('Vegetarian', 'Vegetarian')
    ]

    pizza_type = forms.ChoiceField(choices=PIZZA_TYPES, label='Pizza Types', initial='Pepperoni', widget=forms.Select(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Your message', widget=forms.Textarea(attrs={'class': 'form-control'}))
