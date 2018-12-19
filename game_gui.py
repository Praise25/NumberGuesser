import tkinter
import random
import stages
import errors

# Initialising the variables so that they can be manipulated by the functions and be re-used by other functions
difficulty_value = 0
a = 0
b = 0
tries = stages.tries
diff = ""
answer = 0


def create_label(window, text, row, column, sticky='w', padx=0, pady=0):
    tkinter.Label(window, text=text).grid(row=row, column=column, sticky=sticky, padx=padx, pady=pady)


def new_game():

    def start_game():
        nonlocal promptWindow

        promptWindow.destroy()
        select_difficulty()
        play_game()

    def thanks():
        nonlocal promptWindow

        promptWindow.destroy()
        promptWindow = tkinter.Tk()
        promptWindow.geometry("150x70+500+250")
        promptWindow["padx"] = 10
        promptWindow["pady"] = 10

        # Thank you message displayed to the player
        tkinter.Label(promptWindow, text="Thank you for playing :)").grid(row=0, column=0, sticky="ew")

        # Ok Button
        tkinter.Button(promptWindow, text="Ok", command=promptWindow.destroy).grid(row=1, column=0, sticky='ew')

        # Prevents the window from being re-sized beyond what has been set
        promptWindow.minsize(width=150, height=70)
        promptWindow.maxsize(width=150, height=70)

        promptWindow.mainloop()

    promptWindow = tkinter.Tk()
    promptWindow.geometry("170x70+500+250")
    promptWindow["padx"] = 10
    promptWindow["pady"] = 10

    # Question to play again displayed to the player
    tkinter.Label(promptWindow, text="Do you wish to play again?").grid(row=0, column=0, sticky="ew", columnspan=2)

    # Yes and No Buttons
    tkinter.Button(promptWindow, text="Yes", command=start_game).grid(row=1, column=0, sticky="ew")
    tkinter.Button(promptWindow, text="No", command=thanks).grid(row=1, column=1, sticky="ew")

    # Prevents the window from being re-sized beyond what has been set
    promptWindow.minsize(width=170, height=70)
    promptWindow.maxsize(width=170, height=70)

    promptWindow.mainloop()


def congratulations():
    promptWindow = tkinter.Tk()
    promptWindow.geometry("230x70+500+250")
    promptWindow.title("Correct!!!")
    promptWindow["padx"] = 10
    promptWindow["pady"] = 10

    # Congratulations message displayed to the player
    tkinter.Label(promptWindow, text="Congratulations!!!  You guessed right :)").grid(row=0, column=0)
    tkinter.Button(promptWindow, text="Nice", command=promptWindow.destroy).grid(row=1, column=0)

    # Prevents the window from being re-sized beyond what has been set
    promptWindow.minsize(width=230, height=70)
    promptWindow.maxsize(width=230, height=70)

    promptWindow.mainloop()


def game_over():
    promptWindow = tkinter.Tk()
    promptWindow.geometry("230x110+500+250")
    promptWindow.title("Game Over")
    promptWindow["padx"] = 10
    promptWindow["pady"] = 10

    # Game over message displayed to the player
    create_label(promptWindow, "GAME OVER!!!", 0, 0, sticky='ew')
    create_label(promptWindow, "Sorry, You've exhausted all your tries :(", 1, 0, sticky='ew')
    create_label(promptWindow, "The number I thought of was {}".format(answer), 2, 0, sticky='ew')

    # Done Button
    tkinter.Button(promptWindow, text="Done", command=promptWindow.destroy).grid(row=4, column=0)

    # Prevents the window from being re-sized beyond what has been set
    promptWindow.minsize(width=230, height=110)
    promptWindow.maxsize(width=230, height=110)

    promptWindow.mainloop()


def select_difficulty():

    def run_stage():
        global difficulty_value
        global a
        global b
        global tries
        global diff
        global answer

        try:
            difficulty_value = int(difficulty_entry.get())
            if difficulty_value in range(1, 6):
                if difficulty_value == 1:
                    stages.easy()
                elif difficulty_value == 2:
                    stages.casual()
                elif difficulty_value == 3:
                    stages.hard()
                elif difficulty_value == 4:
                    stages.vhard()
                elif difficulty_value == 5:
                    stages.impossible()

                # Getting the values from the stages module
                a = stages.a
                b = stages.b
                tries = stages.tries
                diff = stages.diff
                answer = random.randint(a, b)
                inputWindow.destroy()
            else:
                errors.input_error("valid number from the difficulty list", 320)
        except ValueError:
            errors.input_error("valid number from the difficulty list", 320)

    inputWindow = tkinter.Tk()
    inputWindow.geometry("170x200+550+200")
    inputWindow.title("Guess The Number")
    inputWindow["padx"] = 15
    inputWindow["pady"] = 15

    # Frame for the difficulty level listing
    label_frame = tkinter.Frame(inputWindow)
    label_frame.grid(row=0, column=0)

    # Labels listing the difficulty levels available
    create_label(label_frame, "Please select a difficulty", 0, 0)
    create_label(label_frame, "Input 1 for Easy", 1, 0)
    create_label(label_frame, "Input 2 for Casual", 2, 0)
    create_label(label_frame, "Input 3 for Hard", 3, 0)
    create_label(label_frame, "Input 4 for Very Hard", 4, 0)
    create_label(label_frame, "Input 5 for Impossible", 5, 0)

    # Difficulty level entered by the player
    difficulty_entry = tkinter.Entry(inputWindow, width=5)
    difficulty_entry.grid(row=1, column=0, sticky="n")

    # Ok button
    ok_button = tkinter.Button(inputWindow, text="Ok", width=10, command=run_stage)
    ok_button.grid(row=2, column=0, sticky="s", pady=5)

    # Prevents the window from being re-sized beyond what has been set
    inputWindow.minsize(width=170, height=200)
    inputWindow.maxsize(width=170, height=200)

    inputWindow.mainloop()


def play_game():

    def get_guess():
        global a
        global b
        global answer
        global tries

        guess = guess_entry.get()
        # Error handling for the guess given by the user
        try:
            num = int(guess)
            if num < a or num > b:
                errors.guess_error("Out of range", width=140)
            elif num == answer:
                maingameWindow.destroy()
                congratulations()
                new_game()
            else:
                if tries == 0:
                    maingameWindow.destroy()
                    game_over()
                else:
                    tries = tries - 1
                    tries_left.set(tries)
                    # Checking the guess of the user
                    if num < answer:
                        errors.guess_error("Too low. Try again.", width=140)
                    elif num > answer:
                        errors.guess_error("Too high. Try again.", width=140)
                    elif num == answer:
                        errors.guess_error("Correct!!! The number I thought of was " + str(answer))

        except ValueError:
            errors.input_error("valid number")

    maingameWindow = tkinter.Tk()
    maingameWindow.geometry("400x180+550+200")
    maingameWindow.title("Guess The Number")
    maingameWindow["padx"] = 15
    maingameWindow["pady"] = 15

    # Frames to help organize the widgets
    detail_frame = tkinter.Frame(maingameWindow)
    detail_frame.grid(row=0, column=0, sticky='n')

    label_frame = tkinter.Frame(maingameWindow)
    label_frame.grid(row=0, column=1, sticky='n')

    # Text variable holder for the number of tries left to be displayed
    tries_left = tkinter.IntVar()
    tries_left.set(tries)

    # Text variable holder for the difficulty level to be displayed
    difficulty_display = tkinter.StringVar()
    difficulty_display.set(diff)

    # Display label that shows the difficulty level selected
    tkinter.Label(detail_frame, textvariable=difficulty_display).grid(row=0, column=1)

    # Record of the difficulty level and tries left
    create_label(detail_frame, "Difficulty - ", 0, 0, sticky='nw')
    create_label(detail_frame, "Tries left - ", 1, 0)

    # Welcome message displayed to the user
    create_label(label_frame, "Welcome Player!", 0, 0, sticky='ew')
    create_label(label_frame, "I'm thinking of a number between {0} and {1}".format(a, b), 1, 0, padx=5)
    create_label(label_frame, "Guess the number. You have {} tries.".format(tries), 2, 0, padx=5)
    create_label(label_frame, "Take a guess", 3, 0, sticky="ew")

    # Entry box where the user inputs their guess
    guess_entry = tkinter.Entry(maingameWindow, width=10)
    guess_entry.grid(row=1, column=1)

    # The guess button
    guess_button = tkinter.Button(maingameWindow, text="Guess", width=10, command=get_guess)
    guess_button.grid(row=2, column=1, pady=5)

    tries_display = tkinter.Label(detail_frame, textvariable=tries_left)
    tries_display.grid(row=1, column=1, sticky='ew')

    # Prevents the window from being re-sized beyond what has been set
    # If minsize and maxsize are the same, the window gains a permanent size and can't be re-sized
    maingameWindow.minsize(width=400, height=180)
    maingameWindow.maxsize(width=400, height=180)

    maingameWindow.mainloop()


# Prevents it from running when imported by an external file
if __name__ == "__main__":
    select_difficulty()
    play_game()
