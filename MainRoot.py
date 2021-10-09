from tkinter import *
from MyFrames import first_window, new_question
import random



questions = open("Preguntas/Preguntas.txt", "r", encoding="utf-8").read()   
questions = questions.split("Categoria:")
questions.pop(0)
questionsAux = list()
for element in range(0, 5):
    questionsAux.append(questions[element])
questions = list()
for category in questionsAux:
    try:
        questions.append(category.split("¿"))
    except:
        continue
questionsAux = list()
for i in range(5):
    for j in range(1, 6):
        try:
            questionsAux.append(questions[i][j])
        except:
            continue

firstWindow = first_window()

if (firstWindow.closed == True):
    
    Category = 1
    question_count = 0
    question_container = list()
    back_tail = 0
    front_tail = 5
    game_over = False

    for round in range(5):        
        if (game_over == True):
            break
        containerAux = questionsAux[back_tail:front_tail]
        print(containerAux)
        for questionNumber in range(5):
            
            if (game_over == True):
                break
            
            while True:
                aux = random.choice(containerAux)
                if aux not in question_container:
                    question_container.append(aux)
                    question_count += 1
                    if ( len(question_container) % 5 ) == 0:
                        back_tail += 5
                        front_tail += 5
                        Category += 1
                        break
                    break
                else:
                    continue
            
            try:
                if (question.wants_to_exit == True):
                    break
                else:
                    question = new_question(aux, Category, int(question_count))
                    game_over = question.game_over
                    print("La respuesta correcta es", question.right_answer)
            except:
                question = new_question(aux, Category, int(question_count))
                game_over = question.game_over
                print("La respuesta correcta es", question.right_answer)
            
        continue
    






