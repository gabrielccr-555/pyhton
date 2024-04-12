# Magic 8Ball
# Gabriel Rodrigues
# Made on PyCharm IDE

import random
name = str(input('What is your name? ')).strip()
question = str(input('What is your question? ')).strip()
random_number = random.randint(1, 9)
answer = ''
if random_number == 1:
    answer = 'Yes - definitely'
elif random_number == 2:
    answer = 'It is decidedly no'
elif random_number == 3:
    answer = 'Without a doubt'
elif random_number == 4:
    answer = 'Reply hazy, try again'
elif random_number == 5:
    answer = 'Ask again later'
elif random_number == 6:
    answer = 'Better not tell you now'
elif random_number == 7:
    answer = 'My sources say no'
elif random_number == 8:
    answer = 'Outlook not so good'
elif random_number == 9:
    answer = 'Very doubtful'
else:
    answer = 'Error'
if name == '':
    print('Question: {}'.format(question))
else:
    print('{} asks: {}'.format(name, question))
print('Magic 8-Ball answer: {}'.format(answer))
