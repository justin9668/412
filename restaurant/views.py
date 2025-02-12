# File: views.py
# Author: Justin Wang (justin1@bu.edu), 2/11/2025
# Description: Views

from django.shortcuts import render, redirect

import time
import random

# Create your views here.

def main(request):
    """This view handles the main page."""
    template_name = 'restaurant/main.html'
    return render(request, template_name)

daily_specials = [
    {
        'name': 'oreo_shamrock_mcflurry',
        'item_name': 'OREO® Shamrock McFlurry® - $4.99',
        'image': 'https://s7d1.scene7.com/is/image/mcdonalds/DC_202411_0601_OreoMintMcFlurry_1564x1564?wid=1564&hei=1564&dpr=off'
    },
    {
        'name': 'hamburger_happy_meal',
        'item_name': 'Hamburger Happy Meal® - $5.99',
        'image': 'https://s7d1.scene7.com/is/image/mcdonalds/DC_202307_6975_HamburgerHappyMeal_AppleSlices_WhiteMilkJug1564x1564?wid=1564&hei=1564&dpr=off'
    },
    {
        'name': 'angel_reese_special',
        'item_name': 'The Angel Reese Special - $11.29',
        'image': 'https://s7d1.scene7.com/is/image/mcdonalds/QPC_AngelReeseSpecial_1564x1564?wid=1564&hei=1564&dpr=off'
    }
]

def order(request):
    """This view handles the order page."""
    template_name = 'restaurant/order.html'

    # Get the daily special
    daily_special = random.choice(daily_specials)

    context = {
        'daily_special': daily_special
    }

    return render(request, template_name, context)

def submit_order(request):
    """
    This view handles the submission of the order.
    References: https://docs.djangoproject.com/en/5.1/topics/http/sessions/
    """
    # Check if the request is a POST request
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        items = request.POST.getlist('items')
        special_requests = request.POST['special_requests']

        # Store the form data in the session
        request.session['order_data'] = {
            'name': name,
            'email': email,
            'phone': phone,
            'items': items,
            'special_requests': special_requests
        }

        return redirect('confirmation')
    
    return redirect('order')

prices = {
    'big_mac': 6.69,
    'mcnuggets': 5.79,
    'quarter_pounder': 6.19,
    'fries': 3.99,
    'big_mac_meal': 4.30,
    'mcnuggets_meal': 5.20,
    'quarter_pounder_meal': 4.70,
    'oreo_shamrock_mcflurry': 4.99,
    'hamburger_happy_meal': 5.99,
    'angel_reese_special': 11.29
}

item_names = {
    'big_mac': 'Big Mac®',
    'big_mac_meal': 'Big Mac® Meal',
    'mcnuggets': '10 pc. Chicken McNuggets®',
    'mcnuggets_meal': '10 pc. Chicken McNuggets® Meal',
    'quarter_pounder': 'Quarter Pounder® with Cheese',
    'quarter_pounder_meal': 'Quarter Pounder® with Cheese Meal',
    'fries': 'Medium French Fries',
    'oreo_shamrock_mcflurry': 'OREO® Shamrock McFlurry®',
    'hamburger_happy_meal': 'Hamburger Happy Meal®',
    'angel_reese_special': 'The Angel Reese Special'
}

def confirmation(request):
    """This view handles the confirmation page."""
    template_name = 'restaurant/confirmation.html'

    if request.session.get('order_data'):
        # Get the order data from session
        context = request.session.get('order_data', {})

        # Convert item codes to display names
        context['item_names'] = [item_names[item] for item in context['items']]

        # Calculate the ready time of the order
        readytime = time.time() + (random.randint(30, 60) * 60)
        context['readytime'] = time.strftime('%I:%M %p', time.localtime(readytime))

        # Calculate the total price of the order
        total_price = 0
        for item in context['items']:
            total_price += prices[item]
        context['total_price'] = "{:.2f}".format(total_price)

    else:
        return redirect('order')
    
    return render(request, template_name, context)