import csv
from random import shuffle

print('Welcome to the Quiz Game!')

quiz_subjects = ['Python', 'Mathematics', 'SQL']

for i, subject in enumerate(quiz_subjects):
    print(f'{i+1}. {subject}')

selected_subject = input('Please enter option no: ')

if selected_subject == '1':
    filename = 'data/python_quiz.csv'
elif selected_subject == '2':
    filename = 'data/math_quiz.csv'
elif selected_subject == '3':
    filename = 'data/sql_quiz.csv'
else:
    print("You entered invalid option")
    quit()

print('')
quiz = []
with open(filename, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        options = [
            f'A. {row['Option A']}',
            f'B. {row['Option B']}',
            f'C. {row['Option C']}',
            f'D. {row['Option D']}'
        ]
        quiz.append({
            'question': row['Question'],
            'options': options,
            'answer': row['Correct Answer']
        })

shuffle(quiz)

available_options = ['A', 'B', 'C', 'D']
user_answers = []
score = 0
answer = ''
for q in quiz:
    print(q['question'])
    for o in q['options']:
        print(o)
        
    is_invalid_opt = False
    while(answer not in available_options):
        if is_invalid_opt:
            print('Invalid Option!')
        answer = input('Answer: ').upper()
        is_invalid_opt = True
    if q['answer'] == answer:
        score += 1
        user_answers.append(answer)
        print('\nCorrect!\n')
    else:
        print('\nWrong!')
        print(f'\nCorrect Answer: {q['answer']}\n')
    print('-------------------------------------\n')
    answer = ''
        
print(f'You got {score} out of 5 correct!')