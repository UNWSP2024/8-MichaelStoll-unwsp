#title:capitals quiz
#author: michael stoll
#date: 3/17/2025
import random
score = 0
play_again = 'true'
capitals = {'England': 'London', 'France': 'Paris', 'Germany': 'Berlin', 'Spain': 'Madrid',
            'Italy': 'Rome', 'Greece': 'Athens', 'Albania': 'Tirana', 'Bulgaria': 'Sofia'}

while play_again == 'true':
    question = random.choice(list(capitals.keys()))
    print(f'What is the capital of {question}?')

    if question == 'England':
        correct_answer = 'London'
    elif question == 'France':
        correct_answer = 'Paris'
    elif question == 'Germany':
        correct_answer = 'Berlin'
    elif question == 'Spain':
        correct_answer = 'Madrid'
    elif question == 'Italy':
        correct_answer = 'Rome'
    elif question == 'Greece':
        correct_answer = 'Athens'
    elif question == 'Albania':
        correct_answer = 'Tirana'
    else:
        correct_answer = 'Sofia'

    answer = input('Enter answer:')
    if answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is", correct_answer)
    print('Score is', score, 'point(s)')
    play_again = str(input('Enter \"true\" if you want to play again:'))
