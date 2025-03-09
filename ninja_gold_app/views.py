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


# def process_money(request):
#     print("The form has been submitted!")
#     print(request.POST)
#     building = request.POST['building']

#     if building in request.session['used_buildings']:
#         request.session['activites'].append(
#             f"You have already used the {building.capitalize()}! Choose another building.")
#         return redirect('/')

#     if building == 'farm':
#         num = random.randint(10, 20)
#         request.session['gold'] += num
#         request.session['activites'].append(
#             f"You Found {num} ounces of Gold on a Farm! Yay!")

#     elif building == 'cave':
#         num = random.randint(5, 10)
#         request.session['gold'] += num
#         request.session['activites'].append(
#             f"You Discovered {num} ounces of Gold in a Cave! Yay!")

#     elif building == 'house':
#         num = random.randint(2, 5)
#         request.session['gold'] += num
#         request.session['activites'].append(
#             f"You Stolen {num} ounces of Gold from a House! Yay!")

#     elif building == 'casino':
#         # Customizing probability for losing or winning
#         num = random.choices(
#             population=[random.randint(-50, -1), random.randint(1, 50), 0],
#             # 60% chance to lose, 30% to win, 10% to earn nothing
#             weights=[60, 30, 10],
#             k=1
#         )[0]  # random.choices returns a list, so extract the first element

#         request.session['gold'] += num
#         if num > 0:
#             request.session['activites'].append(
#                 f"You Won {num} ounces of Gold at the Casino! Yay!")
#         elif num == 0:
#             request.session['activites'].append(
#                 "You Won nothing at the Casino. Oh Well...")
#         else:
#             request.session['activites'].append(
#                 f"You Lost {abs(num)} ounces of Gold at the Casino! Boooo!!")

#     # elif building == 'casino':
#     #     num = random.randint(-50, 50)
#     #     request.session['gold'] += num
#     #     if num > 0:
#     #         request.session['activites'].append(
#     #             f"You Won {num} ounces of Gold at the Casino! Yay!")
#     #     elif num == 0:
#     #         request.session['activites'].append("You earned nothing")
#     #     else:
#     #         request.session['activites'].append(
#     #             f"You Lost {abs(num)} ounces of Gold at the Casino! Boooo!!")

#     # Mark the building as used
#     request.session['used_buildings'].append(building)
#     request.session.modified = True  # Ensure session is saved

#     return redirect('/')

def process_money(request):
    print("The form has been submitted!")
    print(request.POST)
    building = request.POST['building']

    # Initialize 'used_buildings' in the session if it doesn't exist
    if 'used_buildings' not in request.session:
        request.session['used_buildings'] = []

    # Check if the building has already been used
    if building in request.session['used_buildings']:
        # Skip processing without appending any message to activities
        request.session.modified = True
        return redirect('/')

    # Check if the building is 'casino' and the user has no gold
    if building == 'casino' and request.session.get('gold', 0) <= 0:
        # Add a message to activities instead of processing the casino
        request.session['activites'].append(
            "No Gold! No Casino! Search another area."
        )
        request.session.modified = True
        return redirect('/')

    # Regular building logic
    if building == 'farm':
        num = random.randint(20, 30)
        request.session['gold'] += num
        request.session['used_buildings'].append('farm')  # Mark as used
        request.session['activites'].append(
            f"You Found {num} ounces of Gold on a Farm! Yay!")

    elif building == 'cave':
        num = random.randint(30, 50)
        request.session['gold'] += num
        request.session['used_buildings'].append('cave')  # Mark as used
        request.session['activites'].append(
            f"You Found {num} ounces of Gold in a Cave! Yay!")

    elif building == 'house':
        num = random.randint(2, 10)
        request.session['gold'] += num
        request.session['used_buildings'].append('house')  # Mark as used
        request.session['activites'].append(
            f"You Stole {num} ounces of Gold from a House! Yay!")

    elif building == 'casino':
        # If user has enough gold, process the casino logic
        num = random.choices(
            population=[random.randint(-50, -1), random.randint(1, 50), 0],
            # 70% chance to lose, 20% chance to win, 10% nothing
            weights=[70, 20, 10],
            k=1
        )[0]  # Extract the random number result

        request.session['gold'] += num
        if num > 0:
            request.session['activites'].append(
                f"You Won {num} ounces of Gold at the Casino! Yay!")
        elif num == 0:
            request.session['activites'].append(
                "You Won nothing at the Casino. Oh Well...")
        else:
            request.session['activites'].append(
                f"You Lost {abs(num)} ounces of Gold at the Casino! Boooo!!")

    # Mark the building as used and ensure session updates are saved
    request.session.modified = True
    return redirect('/')


def reset(request):
    request.session.clear()
    return redirect('/')
