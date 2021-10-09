from tkinter import *
import random

class new_question:

    Question = ""
    Correct = False
    wants_to_exit = False

    def __init__(self, question, category, counter):
        self.Question = question
        root = Tk()
        root.title(f"Sofka U - Ronda {category}, Pregunta {counter}")
        root.iconbitmap("Retos_AprendeConAlf/Ficheros_Ejercicios/Reto_Sofka_PyR/Icons/SofkaU_Icon.ico")  
        root.geometry("650x350")
        MyFrame = Frame(root, padx=10, pady=10)
        MyFrame.pack()
        self.Question = question
        QuestionLabel = Label(MyFrame, text=self.Question)
        QuestionLabel.grid(row=1, column=1)
        

        def Exit_window():
            self.wants_to_exit = True
            root.destroy()
        MyButtonClose = Button(MyFrame, text="Salir", padx=10, pady=5, command=Exit_window)
        MyButtonClose.grid(row=3, column=3)

        def next_window():
            root.destroy()
        MyButtonContinue = Button(MyFrame, text="Continuar", padx=5, command=next_window)
        MyButtonContinue.grid(row=3, column=4)

        root.mainloop()


class first_window:

    closed = False

    def __init__(self):

        
        root = Tk()
        root.title("Preguntas y Respuestas - Sofka U")
        root.iconbitmap("Retos_AprendeConAlf/Ficheros_Ejercicios/Reto_Sofka_PyR/Icons/SofkaU_Icon.ico")  
        MyFrame = Frame(root, padx=10, pady=10)
        MyFrame.pack()
        MyLabel = Label(MyFrame, text=open("Retos_AprendeConAlf/Ficheros_Ejercicios/Reto_Sofka_PyR/Introduccion.txt", "r", encoding="utf-8").read())
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

