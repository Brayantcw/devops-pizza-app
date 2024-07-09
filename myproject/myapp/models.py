from django.db import models

class Contact(models.Model):
    PIZZA_TYPES = [
        ('Margherita', 'Margherita'),
        ('Pepperoni', 'Pepperoni'),
        ('Vegetarian', 'Vegetarian')
    ]

    pizza_type = models.CharField(max_length=50, choices=PIZZA_TYPES, default='Pepperoni')
    message = models.TextField()

    def __str__(self):
        return self.pizza_type
