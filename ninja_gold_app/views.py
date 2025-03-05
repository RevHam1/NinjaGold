import random

from django.shortcuts import HttpResponse, redirect, render


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activites' not in request.session:
        request.session['activites'] = []
    return render(request, 'index.html')


def process_money(request):
    print("The form has been submitted!")
    print(request.POST)
    if request.POST['building'] == 'farm':
        num = random.randint(10, 20)
        request.session['gold'] += num
        request.session['activites'].append(
            "You Found " + str(num) + " ounces of Gold on a Farm! Yay!")

    elif request.POST['building'] == 'cave':
        num = random.randint(5, 10)
        request.session['gold'] += num
        request.session['activites'].append(
            "You Discovered " + str(num) + " ounces of Gold in a Cave! Yay!")

    elif request.POST['building'] == 'house':
        num = random.randint(2, 5)
        request.session['gold'] += num
        request.session['activites'].append(
            "You Stolen " + str(num) + " ounces of Gold from a House! Yay!")

    elif request.POST['building'] == 'casino':
        num = random.randint(-50, 50)
        request.session['gold'] += num
        if num > 0:
            request.session['activites'].append(
                "You Won " + str(num) + " ounces of Gold in the Casino! Yay!")
        elif num == 0:
            request.session['activites'].append("You earned nothing")
        else:
            request.session['activites'].append(
                "You Lost " + str(abs(num)) + " ounces of Gold in the Casino! Boooo!!")
    return redirect('/')


def reset(request):
    request.session.clear()
    return redirect('/')
