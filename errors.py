import tkinter


def create_window(window, width):
    window.title("Warning")
    window.geometry("{}x80+500+250".format(width))
    window["padx"] = 5
    window["pady"] = 5
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    window.maxsize(width=width, height=80)
    window.minsize(width=width, height=80)


def input_error(value, width=230):
    errorWindow = tkinter.Tk()

    create_window(errorWindow, width)

    warning_label = tkinter.Label(errorWindow, text="Please input a {}".format(value))
    warning_label.grid(row=0, column=0, sticky="ew")

    cancel_button = tkinter.Button(errorWindow, text="Cancel", command=errorWindow.destroy)
    cancel_button.grid(row=1, column=0, sticky="n")

    errorWindow.mainloop()


def guess_error(value, width=230):
    errorWindow = tkinter.Tk()

    create_window(errorWindow, width)

    warning_label = tkinter.Label(errorWindow, text="{}".format(value))
    warning_label.grid(row=0, column=0, sticky="ew")

    cancel_button = tkinter.Button(errorWindow, text="Cancel", command=errorWindow.destroy)
    cancel_button.grid(row=1, column=0, sticky="n")

    errorWindow.mainloop()