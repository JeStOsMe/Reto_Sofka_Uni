from tkinter import *
from MyFrames import first_window, new_question, between_right_answer
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


def between_answer(change_category, points):

    between = between_right_answer(change_category, points)

    if between.Surrender == True:
        return 1
    elif between.Retreat == True:
        return 2
    elif between.Next_question == True:
        return 3


if (firstWindow.closed == True):
    
    Category = 1
    aux_category = Category
    optionReturned = None
    question_count = 0
    question_container = list()
    back_tail = 0
    front_tail = 5
    game_over = False
    points_until_now = 0

    for round in range(5):        
        
        if (game_over == True):
            break
        
        containerAux = questionsAux[back_tail:front_tail]
        
        for questionNumber in range(5):
            
            if (game_over == True):
                break
            
            while True:

                if (game_over == True):
                    break

                aux = random.choice(containerAux)
                if aux not in question_container:
                    question_container.append(aux)
                    question_count += 1
                    if ( len(question_container) % 5 ) == 0:
                        break
                    break
                else:
                    continue
            
            try:
                if (question.wants_to_exit == True):
                    game_over = question.wants_to_exit
                    break
                else:
                    question = new_question(aux, Category, int(question_count))
                    game_over = question.game_over
                    print("!!! La respuesta correcta es", question.right_answer)
            except:
                question = new_question(aux, Category, int(question_count))
                game_over = question.game_over
                print("*** La respuesta correcta es", question.right_answer)
            
            if ( len(question_container) % 5) == 0:
                back_tail += 5
                front_tail += 5
                Category += 1

            if (question.points == 0):
                #Construir ventana de fin del juego
                game_over = True
                print("Fin del juego")
                break
            else:
                points_until_now += 4
                game_over = False
                print("Puntos hasta ahora:", points_until_now)

                if (aux_category != Category):
                    aux_category = Category
                    optionReturned = between_answer(1, points_until_now)
                else:
                    optionReturned = between_answer(0, points_until_now)
            
            if (optionReturned == 1):
                game_over = True
                #Ventana de fin del juego por rendirse
                print("Opción 1")
                break
            elif (optionReturned == 2):
                game_over = True
                #Ventana de fin del juego por retirarse
                print("Opción 2")
                break
            elif (optionReturned == 3):
                game_over = False
                print("Opción  3")
            
        continue
    






