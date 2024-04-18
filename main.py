#Importing the necessary libraries 
from tkinter import *
from tkinter.messagebox import *
import random

#Creating the main app window
root = Tk()
root.title("Guess the number!")
root.resizable(0,0)
root.geometry("400x200")

#Creating the variables for the number to guess and the attempts counter
counter = 0
answer = random.randint(1, 100)

#Defining the logic for the game
def num_guesser():
    # The counter and answer variables were declared outside of the 
    # function because if they were declared inside, everytime the button
    # is clicked, they restart, to avoid that, we just declare them outside
    # the function and call them with the global statement to manipulate their value inside the function
    global counter
    global answer
    guess = data_entry.get()
    # We create an exception here to prevent the program from crashing if the user inputs
    # a float or a string data
    try:
        guess = int(guess)
        if guess > 100:
            showwarning("Warning", "Your number cannot be greater than 100")
            data_entry.delete(0, END)
        elif guess > answer:
            showinfo("Oopsies", f"The answer is less than {guess}")
            data_entry.delete(0, END)
            counter += 1
        elif guess < answer:
            showinfo("Oopsies", f"The answer is higher than {guess}")
            data_entry.delete(0, END)
            counter +=1
        elif guess == answer:
            data_entry.delete(0, END)
            counter += 1
            total_attemps = counter
            showinfo("Win", f"The answer is {answer}, you win!!!\n It took you only {total_attemps} attemps")
            counter = 0
            answer = random.randint(1, 100)
    except ValueError or TypeError as e:
        e = showerror("Error", "You can only enter numbers!")

#Here we create the graphic interface with Tkinter
label_1 = Label(root, text="Enter a number between 1 and 100",
                font='roboto')
label_1.pack(anchor=N, pady=10)

data_entry = Entry(root)
data_entry.pack(anchor=CENTER, pady=10)

submit = Button(root, text="Submit answer!",
                command= lambda : num_guesser(), font='roboto')
submit.pack(anchor=S, pady=10)

root.mainloop()