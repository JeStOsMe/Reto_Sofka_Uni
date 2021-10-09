from tkinter import *
import random
from tkinter import font

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
        root.geometry("650x350")
        MyFrame = Frame(root, padx=10, pady=10)
        MyFrame.pack()
        
        question = question.split("*.")
        self.Question = question

        varOption = IntVar()
        optionOne = Radiobutton(MyFrame, text=self.saving_answer(self.Question[1].strip(), 1), variable=varOption, value=1)
        optionTwo = Radiobutton(MyFrame, text=self.saving_answer(self.Question[2].strip(), 2), variable=varOption, value=2)
        optionThree = Radiobutton(MyFrame, text=self.saving_answer(self.Question[3].strip(), 3), variable=varOption, value=3)
        optionFour = Radiobutton(MyFrame, text=self.saving_answer(self.Question[4].strip(), 4), variable=varOption, value=4)
        
        
        QuestionLabel = Label(MyFrame, text=f"¿{self.Question[0]}")
        QuestionLabel.grid(row=1, column=1, columnspan=4)

        optionOne.grid(row=2, column=1)
        optionTwo.grid(row=3, column=1)
        optionThree.grid(row=4, column=1)
        optionFour.grid(row=5, column=1)

        

        def Exit_window():
            self.wants_to_exit = True
            self.points = 0
            root.destroy()
        MyButtonClose = Button(MyFrame, text="Salir", padx=10, pady=5, command=Exit_window)
        MyButtonClose.grid(row=6, column=3)

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
        MyButtonContinue = Button(MyFrame, text="Responder", padx=10, pady=5, command=lambda:answer_question())
        MyButtonContinue.grid(row=6, column=4)

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
        root.geometry("650x350")
        MyFrame = Frame(root, padx=10, pady=10)
        MyFrame.pack()
        MyLabel = Label(MyFrame, text=open("Introduccion.txt", "r", encoding="utf-8").read())
        MyLabel.grid(row=2, column=0)

        def returnResponse():
            self.closed = True
            root.destroy()

        MyButtonStart = Button(MyFrame, text="Empezar", padx=10, pady=5, command=returnResponse )
        MyButtonStart.grid(row=3, column=4)

        
        def close_window():
            self.closed = False
            root.destroy()
        MyButtonClose = Button(MyFrame, text="Salir", padx=10, pady=5, command=close_window)
        MyButtonClose.grid(row=3, column=3)

        root.mainloop()

class between_right_answer:

    Retreat = False
    Next_question = False
    Surrender = False

    def __init__(self, change_category, points):
        


        root = Tk()
        root.title("Sofka U - Acertaste!")
        root.iconbitmap("Icons/SofkaU_Icon.ico")
        root.geometry("650x350")
        MyFrame = Frame(root, padx=10, pady=10)
        MyFrame.pack()

        LabelOne = Label(MyFrame, text="Felicidades, ha contestado correctamente!", font=30)
        LabelOne.grid(row=2, column=0, columnspan=3)

        def retreat_button():
            self.Retreat = True
            root.destroy()
            
        def next_question():
            self.Next_question = True
            root.destroy()

        def surrender():
            self.Surrender = True
            root.destroy()

        if (change_category == 1):
            LabelTwo = Label(MyFrame, text="Puede retirarse ahora conservando su total de puntos")
            LabelThree = Label(MyFrame, text="O puede continuar a la siguiente pregunta")
            ButtonOne = Button(MyFrame, text="Retirarse", padx=10, pady=10, command=retreat_button)
            ButtonOne.grid(row=6, column=2)
            ButtonTwo = Button(MyFrame, text="Siguiente", padx=10, pady=10, command=lambda:next_question())
            ButtonTwo.grid(row=6, column=3)
        else:
            LabelTwo = Label(MyFrame, text="Puede retirarse sin conservar sus puntos")
            LabelThree = Label(MyFrame, text="O puede continuar a la siguiente pregunta")
            ButtonOne = Button(MyFrame, text="Rendirse", command=surrender)
            ButtonOne.grid(row=6, column=2)
            ButtonTwo = Button(MyFrame, text="Siguiente", command=lambda:next_question())
            ButtonTwo.grid(row=6, column=3)
        LabelTwo.grid(row=3, column=2)
        LabelThree.grid(row=4, column=2)
        LabelFour = Label(MyFrame, text=f"Puntos: {points}", font=20)
        LabelFour.grid(row=5, column=1)





        root.mainloop()

class game_over:


    def __init__(self, end, points, answered_questions):
        root = Tk()
        root.title("Sofka U - Fin del juego")
        root.iconbitmap("Icons/SofkaU_Icon.ico")
        root.geometry("650x350")
        MyFrame = Frame(root, padx=10, pady=10)
        MyFrame.pack()

        def close_window():
            root.destroy()

        if (end == 1):
            #Cuando se equivoca en una pregunta
            print("Game Over")

            LabelOne = Label(MyFrame, text="Has perdido el juego :(", font=30)
            LabelTwo = Label(MyFrame, text=f"Total de puntos: {points}")

        elif (end == 2):
            #Cuando completa las 25 preguntas
            print("Ganador indiscutible")
            LabelOne = Label(MyFrame, text="Has contestado correctamente las 25 preguntas :D", font=30)
            LabelTwo = Label(MyFrame, text=f"Total de puntos: {points}")
        elif (end == 3):
            #Cuando se retira
            LabelOne = Label(MyFrame, text=f"Has contestado correctamente {answered_questions} preguntas :D", font=30)
            LabelTwo = Label(MyFrame, text=f"Total de puntos: {points}")
        
        LabelOne.grid(row=1, column=1, columnspan=2)
        LabelTwo.grid(row=3, column=1, columnspan=2)

        ButtonAccept = Button(MyFrame, text="Aceptar", padx=10, pady=5, command=lambda:close_window())
        ButtonAccept.grid(row=5, column=2)