from tkinter import *


#Clase centrada en la creación de ventanas con una nueva pregunta
class new_question:

    Question = ""
    game_over = False
    wants_to_exit = False
    right_answer=0
    points = 4

    def __init__(self, question, category, counter):
        self.Question = question
        #Creación de la ventana
        root = Tk()
        root.title(f"Sofka U - Ronda {category}, Pregunta {counter}")
        root.iconbitmap("Icons/SofkaU_Icon.ico")  
        root.geometry("650x450")
        root.resizable(False, False)
        
        question = question.split("*.")
        self.Question = question

        img = PhotoImage(file=("SofkaU_Logo.png"))
        labelImg = Label(root, image=img)
        labelImg.place(x=250, y=10)

        varOption = IntVar()    #RadioButtons según las opciones almacenadas en el archivo Preguntas.txt
        optionOne = Radiobutton(root, text=self.saving_answer(self.Question[1].strip(), 1), variable=varOption, value=1, font=20)
        optionTwo = Radiobutton(root, text=self.saving_answer(self.Question[2].strip(), 2), variable=varOption, value=2, font=20)
        optionThree = Radiobutton(root, text=self.saving_answer(self.Question[3].strip(), 3), variable=varOption, value=3, font=20)
        optionFour = Radiobutton(root, text=self.saving_answer(self.Question[4].strip(), 4), variable=varOption, value=4, font=20)
        
        #Pregunta enviada desde MainRoot
        QuestionLabel = Label(root, text=f"¿{self.Question[0]}", font=20)
        
        #Solo un decorador, para que las preguntas más largas intenten estar lo más centradas posible.
        if (len(self.Question[0]) <= 60):
            QuestionLabel.place(x=130, y=180)
        elif (len(self.Question[0]) > 60) and (len(self.Question[0]) <= 70):
            QuestionLabel.place(x=90, y=180)
        elif (len(self.Question[0]) > 70) and (len(self.Question[0]) <= 80):
            QuestionLabel.place(x=60, y=180)
        elif (len(self.Question[0]) > 80):
            QuestionLabel.place(x=15, y=180)

        optionOne.place(x=150, y=230)
        optionTwo.place(x=150, y=260)
        optionThree.place(x=150, y=290)
        optionFour.place(x=150, y=320)

        
        #Función encargada de almacenar la intención del jugador por no contestar la pregunta
        def Exit_window():
            self.wants_to_exit = True
            self.points = 0
            root.destroy()
        MyButtonClose = Button(root, text="Salir", padx=10, pady=10, command=Exit_window, font=("", 10, "bold"), borderwidth=2, relief="solid")
        MyButtonClose.place(x=400, y=375)

        #Función dedicada a tomar la respuesta elegida por el usuario y verificar que sea correcta
        def answer_question():
            if (varOption.get() != self.right_answer): #Si es incorrecta, gameover
                #print("Perdió!")
                self.game_over = True
                self.points = 0
                root.destroy()
            else:   #Si es correcta, sigue en el juego.
                #print("Acertó!")
                self.game_over = False
                self.points = 4
                root.destroy()
        MyButtonContinue = Button(root, text="Responder", padx=10, pady=10, command=lambda:answer_question(), font=("", 10, "bold"), borderwidth=2, relief="solid")
        MyButtonContinue.place(x=500, y=375)

        root.mainloop()

    #Toma las opciones disponibles para la pregunta, y almacena la correcta para poder evaluarla
    def saving_answer(self, question, number):
        if ("!" in question):
            question = question.replace("!", "")
            self.right_answer = number
            return question
        else:
            return question

#Primera ventana que el jugador ve. El mensaje se imprime a partir del archivo Introduccion.txt
class first_window:

    closed = False

    def __init__(self):
        #Creación de la ventana        
        root = Tk()
        root.title("Preguntas y Respuestas - Sofka U")
        root.iconbitmap("Icons/SofkaU_Icon.ico")  
        root.geometry("650x450")
        root.resizable(False, False)
        MyLabel = Label(root, text=open("Introduccion.txt", "r", encoding="utf-8").read())
        MyLabel.place(x=75, y=75)

        LabelTittle = Label(root, text="Trivia - ¿Quién quiere ser Sofkiano?", font=("", 20, "bold"))
        LabelTittle.place(x=80, y=25)
        #Si presiona el botón "empezar", significa que quiere empezar a jugar, y empieza el juego.
        def returnResponse():
            self.closed = True
            root.destroy()

        MyButtonStart = Button(root, text="Empezar", padx=10, pady=5, command=returnResponse, font=("", 10, "bold"), borderwidth=2, relief="solid")
        MyButtonStart.place(x=550, y=400)

        #Si presiona el boton "Salir", simplemente se cerrará la ventana y no empezará el juego.
        def close_window():
            self.closed = False
            root.destroy()
        MyButtonClose = Button(root, text="Salir", padx=20, pady=5, command=close_window, font=("", 10, "bold"), borderwidth=2, relief="solid")
        MyButtonClose.place(x=450, y=400)

        root.mainloop()

#Clase centrada en crear las ventanas entre una pregunta y otra, 
#permitiendole al jugador retirarse o no con sus puntos según los parámetros de entrada
class between_right_answer:

    Retreat = False
    Next_question = False
    Surrender = False

    def __init__(self, option, points):
        #Creación de la ventana
        root = Tk()
        root.title("Sofka U - Correcto!")
        root.iconbitmap("Icons/SofkaU_Icon.ico")
        root.geometry("650x450")
        root.resizable(False, False)
        
        img = PhotoImage(file=("SofkaU_Logo.png"))
        labelImg = Label(root, image=img)
        labelImg.place(x=250, y=10)
        
        LabelOne = Label(root, text="Felicidades, ha contestado correctamente!", font=("", 15, "bold"))
        LabelOne.place(x=130, y=175)

        #Función que almacena la intención del jugador por retirarse con sus puntos.
        def retreat_button():
            self.Retreat = True
            root.destroy()
        #Función que almacena la intención del jugador por responder otra pregunta.
        def next_question():
            self.Next_question = True
            root.destroy()
        #Función que almacena la intención del jugador por acabar el juego sin sus puntos.
        def surrender():
            self.Surrender = True
            root.destroy()
        
        #Si la última pregunta contestada fue final de categoría, permite conservar sus puntos
        if (option == 1):
            LabelTwo = Label(root, text="Puede retirarse ahora conservando su total de puntos", font=20)
            LabelThree = Label(root, text="O puede continuar a la siguiente pregunta", font=20)
            ButtonOne = Button(root, text="Retirarse", padx=10, pady=10, command=retreat_button, font=("", 10, "bold"), borderwidth=2, relief="solid")
            ButtonOne.place(x=450, y=400)
            ButtonTwo = Button(root, text="Siguiente", padx=10, pady=10, command=lambda:next_question(), font=("", 10, "bold"), borderwidth=2, relief="solid")
            ButtonTwo.place(x=550, y=400)
        #Si la última pregunta contestada no era final de categoría, solo permite avanzar.
        else:
            LabelTwo = Label(root, text="Puede retirarse sin conservar sus puntos", font=20)
            LabelThree = Label(root, text="O puede continuar a la siguiente pregunta", font=20)
            ButtonOne = Button(root, text="Rendirse", command=surrender, padx=10, pady=10, font=("", 10, "bold"), borderwidth=2, relief="solid")
            ButtonOne.place(x=450, y=400)
            ButtonTwo = Button(root, text="Siguiente", command=lambda:next_question(), padx=10, pady=10, font=("", 10, "bold"), borderwidth=2, relief="solid")
            ButtonTwo.place(x=550, y=400)
        LabelTwo.place(x=180, y=250)
        LabelThree.place(x=180, y=280)
        LabelFour = Label(root, text=f"Puntos acumulados: {points}", font=("", 15, "bold"))
        LabelFour.place(x=50, y=400)

        root.mainloop()

#Clase centrada en crear las ventanas de fin de juego, indicando si ganó o perdió, y las preguntas contestadas
class endgame:

    def __init__(self, end, points, answered_questions):
        #Creación de la ventana
        root = Tk()
        root.title("Sofka U - Fin del juego")
        root.iconbitmap("Icons/SofkaU_Icon.ico")
        root.geometry("650x450")
        root.resizable(False, False)
        
        def close_window():
            root.destroy()

        #Si el parámetro es uno, significa que ha perdido el juego. Adapta Label
        if (end == 1):
            #Cuando se equivoca en una pregunta
            #print("Game Over")
            LabelOne = Label(root, text="Has perdido el juego :(", font=("", 30, "bold"))
            LabelOne.place(x=100, y=50)            

        #Si el parámetro es 2, significa que ha contestado correctamente las 25 preguntas. Adapta Label
        elif (end == 2):
            #Cuando completa las 25 preguntas
            #print("Ganador indiscutible")
            LabelOne = Label(root, text="Has contestado correctamente las 25 preguntas :D", font=("", 20, "bold"))
            LabelOne.place(x=20, y=50)
        #Si el parámetro es 3, significa que se retira del juego.
        elif (end == 3):
            #Cuando se retira
            LabelOne = Label(root, text=f"Has contestado correctamente {answered_questions} preguntas :D", font=("", 20, "bold"))
            LabelOne.place(x=20, y=50)
        
        img = PhotoImage(file=("SofkaU_Logo.png"))
        labelImg = Label(root, image=img)
        labelImg.place(x=250, y=110)

        LabelTwo = Label(root, text=f"Total de puntos:      {points}", font=("", 25, "bold"))
        LabelTwo.place(x=100, y=280)

        ButtonAccept = Button(root, text="Aceptar", padx=10, pady=10, command=close_window, font=("", 15, "bold"), borderwidth=2, relief="solid")
        ButtonAccept.place(x=500, y=380)

        root.mainloop()

#Clase centrada en guardar a los usuarios en un archivo local, según sea el caso.
class save_user:

    username = ""
    points = 0

    def __init__(self, points):
        
        if (points == 0):
            self.print_users()
            return

        root = Tk()
        root.title("Sofka U - Registro de usuario")
        root.iconbitmap("Icons/SofkaU_Icon.ico")
        root.geometry("650x450")
        root.resizable(False, False)

        img = PhotoImage(file=("SofkaU_Logo.png"))
        labelImg = Label(root, image=img)
        labelImg.place(x=250, y=80)
        #Almacena los datos del usuario 
        def save_data_user():
            #print("Guardar usuario")
            self.username = usernameText.get()
            self.points = points
            root.destroy()

        LabelOne = Label(root, text="Guardado de usuario", font=("", 25, "bold"))
        LabelTwo = Label(root, text="Por favor, ingrese un usuario para almacenar", font=30)
        LabelThree = Label(root, text="Usuario:", padx=5, pady=5, font=20)
        usernameText = Entry(root)
        ButtonSave = Button(root, text="Guardar", padx=10, pady=10, command=save_data_user, font=("", 15, "bold"),  borderwidth=2, relief="solid")


        LabelOne.place(x=170, y=10)
        LabelTwo.place(x=150, y=250)
        LabelThree.place(x=100, y=300)
        usernameText.place(x=200, y=310)
        ButtonSave.place(x=500, y=380)


        root.mainloop()

    #Almacena al jugador en el archivo Historico.txt
    def save_username(self):
        
        #print(self.username, "<--->", self.points)
        
        with open("Historico_Jugadores/Historico.txt", "a+", encoding="utf-8") as registro:
            #Lee todas las lineas del archivo Historico.txt y las almacena en forma de lista.
            usuarios = registro.readlines()

            #Un decorador para que todos tengan la misma longitud
            if (len(self.username) > 10):
                usuarios.append(f"Usuario: {self.username[:10]}, \tPuntos: {self.points}\n")
            else:
                while True:
                    if (len(self.username) <= 10):
                        self.username = self.username + " "
                    else:
                        break
                usuarios.append(f"Usuario: {self.username[:10]}, \tPuntos: {self.points}\n")
            #Luego de agregar el jugador nuevo, sobreescribe el archivo Historico.txt 
            for usuario in usuarios:
                registro.write(usuario)
    
    #Imprime todos los jugadores almacenados en el archivo Historico.txt
    def print_users(self):
        with open("Historico_Jugadores/Historico.txt", "r", encoding="utf-8") as registro:
            users = ""
            for line in registro.readlines():
                users += line.replace("{", "").replace("}", "").strip() + "\n"
            
            root = Tk()
            root.title("Sofka U - Registro de Jugadores")
            root.iconbitmap("Icons/SofkaU_Icon.ico")
            root.geometry("650x450")
            root.resizable(False, False)

            usersText = Text(root, font=15, width=50, height=10)
            for line in users:
                usersText.insert(INSERT, line)
            usersText.place(x=120, y=50)

            scroll = Scrollbar(root, command=usersText.yview, width=14)
            scroll.place(in_=usersText, relx=1, relheight=1, bordermode="outside")
            
            exitButton = Button(root, text="Salir", padx=10, pady=5, command=lambda:root.destroy(), font=("", 15, "bold"),  borderwidth=2, relief="solid")
            exitButton.place(x=500, y= 350)
            
            
            root.mainloop()
