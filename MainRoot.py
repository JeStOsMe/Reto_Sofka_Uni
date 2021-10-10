from tkinter import *
from MyFrames import first_window, new_question, between_right_answer, endgame, save_user
import random

#Abro el archivo con las preguntas almacenadas
questions = open("Preguntas/Preguntas.txt", "r", encoding="utf-8").read()   
#Modifico la lista para que contenga 5 elementos correspondientes a las categorías
questions = questions.split("Categoria:")
questions.pop(0)
questionsAux = list()

#Creo una lista auxiliar que contendrá los mismos 5 elementos correspondientes a las categorías
for element in range(0, 5):
    questionsAux.append(questions[element])
questions = list()

#Creo una lista de 2 dimensiones que contendrá las preguntas individualizadas.
for category in questionsAux:
    try:
        questions.append(category.split("¿"))
    except:
        continue
#Preparo la lista que contendrá únicamente las preguntas
questionsAux = list()
for i in range(5):
    for j in range(1, 6):
        try:
            #Agrego únicamente las preguntas con sus respectivas opciones
            questionsAux.append(questions[i][j])
        except:
            continue

#Llamada a la ventana inicial, con la que se verá un texto almacenado en el archivo Introduccion.txt
firstWindow = first_window()

#Función que, al ser llamada, crea un nuevo objeto que creará una ventana que llamé "entre respuestas"
# Esto con el fin de darle a elegir al usuario si salir antes de pasar a la siguiente pregunta.
def between_answer(option, points):

    #El parámetro opción le indica a la clase si imprimirá un mensaje permitiendole salir conservando los puntos acumulados o no.
    #Esto para que el jugador pueda salir con sus puntos una vez acaba la ronda
    between = between_right_answer(option, points)

    #Si se rinde, significa que no pasará a la siguiente pregunta y perderá los puntos
    if between.Surrender == True:
        return 1
    #Si se retira, significa que no pasará a la siguiente ronda y conservará los puntos
    elif between.Retreat == True:
        return 2
    #Si así lo decide, pasará a la siguiente pregunta.
    elif between.Next_question == True:
        return 3

#Según el valor del parámetro, guardará al usuario con sus puntos y luego mostrará el histórico, o solo mostrará el histórico.
def saveUser(points):
    #Si el parámetro vale cero, solo se imprimirán los usuarios.
    if (points == 0):
        user = save_user(0)
        #user.print_users()
        return None
    #Si el parámetro vale alguno de los puntos de ronda, podrá salir y conservar sus puntos, a la vez que es registrado
    elif (points == 20) or (points == 40) or (points == 60) or (points == 80) or (points == 100):
        user = save_user(points)
        user.save_username()
        user.print_users()
    #Si el usuario simplemente decide retirarse antes de completar una ronda, solo imprimirá el histórico.
    else:
        user = save_user(0)
        #user.print_users()

#Dado los parámetros, puede imprimir una pantalla según si se equivocó, se retiró o se rindió.
def end_game(points, option, ans):
    
    final_message = endgame(option, points, ans)

#Si closed es verdadero, significa que el usuario decidió empezar a jugar. Sino, significa que solo presionó salir.
if (firstWindow.closed == True):
    
    Category = 1 #Categoría en la que empieza el juego.
    aux_category = Category #Verificador de categoría.
    optionReturned = None
    question_count = 0      #Contador de preguntas
    question_container = list()     #Contendrá todas las preguntas hechas hasta el momento, asegurando que ninguna se repetirá.
    back_tail = 0       #Junto con cola delantera, aseguran que las preguntas a realizar pertenezcan a una categoría específica
    front_tail = 5
    game_over = False   #Si es verdadero, el juego acaba indiscutiblemente
    points_until_now = 0    #Acumulado de puntos.

    #Ciclo de 5 iteraciones para 5 categorías
    for round in range(5):        
        
        if (game_over == True):
            break
        
        #Toma las 5 preguntas de la categoría inicial.
        containerAux = questionsAux[back_tail:front_tail]
        
        #Ciclo de 5 iteraciones para 5 preguntas.
        for questionNumber in range(5):
            
            if (game_over == True):
                break
            
            #Ciclo para asegurar que la pregunta escogida, no haya salido ya. 
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
            
            #Si el jugador decide salir, el juego termina.
            try:
                if (question.wants_to_exit == True):
                    game_over = question.wants_to_exit
                    #print("Quiere salir")
                    break
                else: #Si no quiere salir, se lanza la pregunta.
                    question = new_question(aux, Category, int(question_count))
                    game_over = question.game_over
                    #print("!!! La respuesta correcta es", question.right_answer)
            except: #Si no quiere salir, se lanza la pregunta.
                question = new_question(aux, Category, int(question_count))
                game_over = question.game_over
                #print("*** La respuesta correcta es", question.right_answer)
            
            #Si ya se han hecho 5 preguntas, se pasa de categoría
            if ( len(question_container) % 5) == 0:
                back_tail += 5
                front_tail += 5
                Category += 1
            #Si luego de contestar la pregunta, resulta que se equivocó: fin del juego.
            if (question.points == 0):
                #Construye ventana de fin del juego
                game_over = True
                #print("Se ha equivocado")
                #Si se equivocó, llama a la ventana de fin de juego.
                end_game(points_until_now, 1, question_count)
                saveUser(0)
                break
            else: #Si contesta bien, se pasa a evaluar.
                points_until_now += 4
                game_over = False
                #print("Puntos hasta ahora:", points_until_now)

                #Si tiene 100 puntos, significa que ha ganado el juego.
                if (points_until_now == 100):
                    game_over = True
                    end_game(points_until_now, 2, question_count)
                    saveUser(points_until_now)
                    break
                
                #Debido a que cada 5 preguntas se cambia de categoría, debe evaluarse que lo esté haciendo.
                if (aux_category != Category):
                    aux_category = Category
                    #Si cambió de categoría, imprime ventana permitiendo salir con los puntos.
                    optionReturned = between_answer(1, points_until_now)
                else:
                    #Si no cambió categoría, imprime ventana indicando los puntos hasta ahora.
                    optionReturned = between_answer(0, points_until_now)
            
            
            if (optionReturned == 1): #En caso de que se rinda, se acaba el juego
                game_over = True
                #Ventana de fin del juego por rendirse
                #print("Opción 1")
                end_game(points_until_now, 1, question_count)
                saveUser(points_until_now)
                break
            elif (optionReturned == 2):     #En caso de que se retire, se acaba el juego.
                game_over = True
                #Ventana de fin del juego por retirarse
                #print("Opción 2")
                end_game(points_until_now, 3, question_count)
                saveUser(points_until_now)
                break
            
        continue
    






