"""
This module contains the model definitions for the myapp application.
"""

from django.db import models

class Orders(models.Model):
    """
    Class to handle the Orders info
    """
    PIZZA_TYPES = [
        ('Margherita', 'Margherita'),
        ('Pepperoni', 'Pepperoni'),
        ('Vegetarian', 'Vegetarian')
    ]

    name = "Orders"
    pizza_type = models.CharField(max_length=50, choices=PIZZA_TYPES, default='Pepperoni')
    message = models.TextField()

    def __str__(self):
        return self.name
