from tkinter import *

class new_question:

    Question = ""
    game_over = False
    wants_to_exit = False
    right_answer=0
    points = 4

    def __init__(self, question, category, counter):
        self.Question = question
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

        varOption = IntVar()
        optionOne = Radiobutton(root, text=self.saving_answer(self.Question[1].strip(), 1), variable=varOption, value=1, font=20)
        optionTwo = Radiobutton(root, text=self.saving_answer(self.Question[2].strip(), 2), variable=varOption, value=2, font=20)
        optionThree = Radiobutton(root, text=self.saving_answer(self.Question[3].strip(), 3), variable=varOption, value=3, font=20)
        optionFour = Radiobutton(root, text=self.saving_answer(self.Question[4].strip(), 4), variable=varOption, value=4, font=20)
        
        
        QuestionLabel = Label(root, text=f"¿{self.Question[0]}", font=20)
        
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

        

        def Exit_window():
            self.wants_to_exit = True
            self.points = 0
            root.destroy()
        MyButtonClose = Button(root, text="Salir", padx=10, pady=10, command=Exit_window, font=("", 10, "bold"), borderwidth=2, relief="solid")
        MyButtonClose.place(x=400, y=375)

        def answer_question():
            if (varOption.get() != self.right_answer):
                print("Perdió!")
                self.game_over = True
                self.points = 0
                root.destroy()
            else:
                print("Acertó!")
                self.game_over = False
                self.points = 4
                root.destroy()
        MyButtonContinue = Button(root, text="Responder", padx=10, pady=10, command=lambda:answer_question(), font=("", 10, "bold"), borderwidth=2, relief="solid")
        MyButtonContinue.place(x=500, y=375)

        root.mainloop()

    def saving_answer(self, question, number):
        if ("!" in question):
            question = question.replace("!", "")
            self.right_answer = number
            return question
        else:
            return question

class first_window:

    closed = False

    def __init__(self):

        
        root = Tk()
        root.title("Preguntas y Respuestas - Sofka U")
        root.iconbitmap("Icons/SofkaU_Icon.ico")  
        root.geometry("650x450")
        root.resizable(False, False)
        MyLabel = Label(root, text=open("Introduccion.txt", "r", encoding="utf-8").read())
        MyLabel.place(x=75, y=75)

        LabelTittle = Label(root, text="Trivia - ¿Quién quiere ser Sofkiano?", font=("", 20, "bold"))
        LabelTittle.place(x=80, y=25)

        def returnResponse():
            self.closed = True
            root.destroy()

        MyButtonStart = Button(root, text="Empezar", padx=10, pady=5, command=returnResponse, font=("", 10, "bold"), borderwidth=2, relief="solid")
        MyButtonStart.place(x=550, y=400)

        
        def close_window():
            self.closed = False
            root.destroy()
        MyButtonClose = Button(root, text="Salir", padx=20, pady=5, command=close_window, font=("", 10, "bold"), borderwidth=2, relief="solid")
        MyButtonClose.place(x=450, y=400)

        root.mainloop()

class between_right_answer:

    Retreat = False
    Next_question = False
    Surrender = False

    def __init__(self, option, points):
        


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

        def retreat_button():
            self.Retreat = True
            root.destroy()
            
        def next_question():
            self.Next_question = True
            root.destroy()

        def surrender():
            self.Surrender = True
            root.destroy()

        if (option == 1):
            LabelTwo = Label(root, text="Puede retirarse ahora conservando su total de puntos", font=20)
            LabelThree = Label(root, text="O puede continuar a la siguiente pregunta", font=20)
            ButtonOne = Button(root, text="Retirarse", padx=10, pady=10, command=retreat_button, font=("", 10, "bold"), borderwidth=2, relief="solid")
            ButtonOne.place(x=450, y=400)
            ButtonTwo = Button(root, text="Siguiente", padx=10, pady=10, command=lambda:next_question(), font=("", 10, "bold"), borderwidth=2, relief="solid")
            ButtonTwo.place(x=550, y=400)
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

class endgame:


    def __init__(self, end, points, answered_questions):
        root = Tk()
        root.title("Sofka U - Fin del juego")
        root.iconbitmap("Icons/SofkaU_Icon.ico")
        root.geometry("650x450")
        root.resizable(False, False)

        def close_window():
            root.destroy()

        if (end == 1):
            #Cuando se equivoca en una pregunta
            print("Game Over")

            LabelOne = Label(root, text="Has perdido el juego :(", font=("", 30, "bold"))
            LabelOne.place(x=100, y=50)            

        elif (end == 2):
            #Cuando completa las 25 preguntas
            print("Ganador indiscutible")
            LabelOne = Label(root, text="Has contestado correctamente las 25 preguntas :D", font=("", 20, "bold"))
            LabelOne.place(x=20, y=50)
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

        def save_data_user():
            print("Guardar usuario")
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

    def save_username(self):
        
        #print(self.username, "<--->", self.points)
        
        with open("Historico_Jugadores/Historico.txt", "a+", encoding="utf-8") as registro:
            
            usuarios = registro.readlines()


            if (len(self.username) > 10):
                usuarios.append(f"Usuario: {self.username[:10]}, \tPuntos: {self.points}\n")
            else:
                while True:
                    if (len(self.username) <= 10):
                        self.username = self.username + " "
                    else:
                        break
                usuarios.append(f"Usuario: {self.username[:10]}, \tPuntos: {self.points}\n")
            
            for usuario in usuarios:
                registro.write(usuario)
    
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
