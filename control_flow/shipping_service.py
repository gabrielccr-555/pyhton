# Sal's Shipping
# Gabriel Rodrigues
# Made on PyCharm IDE

print('-=-'*20)
print('We will assist you on picking the cheapest way to send your package!')
print('-=-'*20)
weight = float(input('Please, inform your package weight, in pounds: '))
# Ground Shipping 🚛
if weight <= 2:
    ground = weight * 1.5 + 20
elif 2 < weight <= 6:
    ground = weight * 3 + 20
elif 6 < weight <= 10:
    ground = weight * 4 + 20
else:
    ground = weight * 4.75 + 20
# Ground Shipping Premium 🚛💨✨
ground_P = 125
# Drone Shipping 🚁
if weight <= 2:
    drone = weight * 4.5
elif 2 < weight <= 6:
    drone = weight * 9
elif 6 < weight <= 10:
    drone = weight * 12
else:
    drone = weight * 14.25
# Best Choice 👍
if ground < ground_P and ground < drone:
    print('The cheapest choice is Ground Shipping')
    print('It will cost you: ${}'.format(ground))
if ground_P < ground and ground_P < drone:
    print('The cheapest choice is Ground Shipping Premium')
    print('It will cost you: ${}'.format(ground_P))
if drone < ground_P and drone < ground:
    print('The cheapest choice is Drone Shipping')
    print('It will cost you: ${}'.format(drone))
