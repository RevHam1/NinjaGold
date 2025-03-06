import random

from django.shortcuts import HttpResponse, redirect, render


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activites' not in request.session:
        request.session['activites'] = []
    if 'used_buildings' not in request.session:
        request.session['used_buildings'] = []
    return render(request, 'index.html')


def process_money(request):
    print("The form has been submitted!")
    print(request.POST)
    building = request.POST['building']

    if building in request.session['used_buildings']:
        request.session['activites'].append(
            f"You have already used the {building.capitalize()}! Choose another building.")
        return redirect('/')

    if building == 'farm':
        num = random.randint(10, 20)
        request.session['gold'] += num
        request.session['activites'].append(
            f"You Found {num} ounces of Gold on a Farm! Yay!")

    elif building == 'cave':
        num = random.randint(5, 10)
        request.session['gold'] += num
        request.session['activites'].append(
            f"You Discovered {num} ounces of Gold in a Cave! Yay!")

    elif building == 'house':
        num = random.randint(2, 5)
        request.session['gold'] += num
        request.session['activites'].append(
            f"You Stolen {num} ounces of Gold from a House! Yay!")

    elif building == 'casino':
        num = random.randint(-50, 50)
        request.session['gold'] += num
        if num > 0:
            request.session['activites'].append(
                f"You Won {num} ounces of Gold at the Casino! Yay!")
        elif num == 0:
            request.session['activites'].append("You earned nothing")
        else:
            request.session['activites'].append(
                f"You Lost {abs(num)} ounces of Gold at the Casino! Boooo!!")

    # Mark the building as used
    request.session['used_buildings'].append(building)
    request.session.modified = True  # Ensure session is saved

    return redirect('/')


def reset(request):
    request.session.clear()
    return redirect('/')
