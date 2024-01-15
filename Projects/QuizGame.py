print('Hello! Welcome to the quiz game.')

playing = input('Are you ready to play?\n')
if playing.lower() != 'yes':
    print("No worries, come back when you're ready!")
    quit()

print('Okay! Its quiz time :)')

question_num = 0
score = 0

def quiz(question, answer):
    global question_num, score
    question_num += 1

    guest_ans = input(question)
    if guest_ans.lower() == answer:
        print('Correct!')
        score += 1
    else:
        print('Incorrect. Better luck next time :( ')
    
quiz('What does CPU stand for? \n', 'central processing unit')
quiz('Which computer software company developed and published the graphics editor Photoshop?\n', 'adobe')
quiz('Name the simple text editor associated with Microsoft Windows?\n', 'notepad')

print("That's the end of the quiz!")
print(f'Your got {score} out of {question_num} questions correct!')

quit()
