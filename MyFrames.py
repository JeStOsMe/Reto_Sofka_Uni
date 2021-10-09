from tkinter import *
import random

class new_question:

    Question = ""
    game_over = False
    wants_to_exit = False
    right_answer=0

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
            root.destroy()
        MyButtonClose = Button(MyFrame, text="Salir", padx=10, pady=5, command=Exit_window)
        MyButtonClose.grid(row=6, column=3)

        def answer_question():
            if (varOption.get() != self.right_answer):
                print("Perdió!")
                self.game_over = True
                root.destroy()
            else:
                print("Acertó!")
                self.game_over = False
            
        MyButtonContinue = Button(MyFrame, text="Responder", padx=5, command=lambda:answer_question())
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

