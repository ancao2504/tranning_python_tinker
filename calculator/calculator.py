from ast import operator
from tkinter import *
from playsound import playsound

# function
def butonClick(number):
    global operator
    # for playing note.mp3 file
    try:
        playsound('tit.wav')
        print('playing sound using  playsound')
        operator = operator + str(number)
        text_input.set(operator)
    except:
        operator.set(" error play sound")


# add
def add(x, y):
    return x + y


def buttonEquals():
    try:
        global operator
        result = str(eval(operator))
        text_input.set(result)

         # by empty string
        operator = ""
    except:
        operator.set(" error ")
        operator = ""

def buttonClear():
    global operator
    text_input.set("")


if __name__ == "__main__":

    root = Tk()
    #set icon
    root.iconbitmap('python.ico')


    root.title("Calculator")
    operator = ''
    text_input = StringVar()
    txtDisplay = Entry(
        root, 
        width=30, 
        font=('arial', 20, 'bold'), 
        textvariable=text_input, 
        bd= 15, 
        insertwidth=4, 
        bg='#0052cc', 
        fg='#ffffff',
        justify='right').grid(columnspan=4)
    # vẽ các nút 7, 8, 9, -
    button_7 = Button(
        root, 
        padx=30, 
        bd=8, 
        fg="black",
        font=('arial', 20, 'bold'),
        text="7",
        command=lambda:butonClick(7),
        bg="silver"
        
        ).grid(row=1, column=0)
    button_8 = Button(
        root, 
        padx=30, 
        bd=8, 
        fg="black",
        font=('arial', 20, 'bold'),
        text="8",
        command=lambda:butonClick(8),
        bg="silver"
        ).grid(row=1, column=1)
    button_9 = Button(
        root, 
        padx=30, 
        bd=8, 
        fg="black",
        font=('arial', 20, 'bold'),
        text="9",
        command=lambda:butonClick(9),
        bg="silver"
        ).grid(row=1, column=2)
    button_add = Button(
        root, 
        padx=30, 
        bd=8, 
        fg="black",
        font=('arial', 20, 'bold'),
        text="+",
        command=lambda:butonClick("+"),
        bg="silver"
        ).grid(row=1, column=3)

    ##############################################################
    button_4 = Button(
        root, 
        padx=30, 
        bd=8, 
        fg="black",
        font=('arial', 20, 'bold'),
        text="4",
        command=lambda:butonClick(4),
        bg="silver"
        ).grid(row=2, column=0)
    button_5 = Button(
        root, 
        padx=30, 
        bd=8, 
        fg="black",
        font=('arial', 20, 'bold'),
        text="5",
        command=lambda:butonClick(5),
        bg="silver"
    ).grid(row=2, column=1)
    button_6 = Button(
        root, 
        padx=30, 
        bd=8, 
        fg="black",
        font=('arial', 20, 'bold'),
        text="6",
        command=lambda:butonClick(6),
        bg="silver"
    ).grid(row=2, column=2)
    button_subtract = Button(
        root, 
        padx=30, 
        bd=8, 
        fg="black",
        font=('arial', 20, 'bold'),
        text="-",
        command=lambda:butonClick("-"),
        bg="silver"
    ).grid(row=2, column=3)
    ##############################################################

    ##############################################################
    button_1 = Button(
        root, 
        padx=30, 
        bd=8, 
        fg="black",
        font=('arial', 20, 'bold'),
        text="1",
        command=lambda:butonClick(1),
        bg="silver"
        ).grid(row=3, column=0)
    button_2 = Button(
        root, 
        padx=30, 
        bd=8, 
        fg="black",
        font=('arial', 20, 'bold'),
        text="2",
        command=lambda:butonClick(2),
        bg="silver"
    ).grid(row=3, column=1)
    button_3 = Button(
        root, 
        padx=30, 
        bd=8, 
        fg="black",
        font=('arial', 20, 'bold'),
        text="3",
        command=lambda:butonClick(3),
        bg="silver"
    ).grid(row=3, column=2)
    button_multiply = Button(
        root, 
        padx=30, 
        bd=8, 
        fg="black",
        font=('arial', 20, 'bold'),
        text="*",
        command=lambda:butonClick("*"),
        bg="silver"
    ).grid(row=3, column=3)
    ##############################################################

    ##############################################################
    button_0 = Button(
        root, 
        padx=30, 
        bd=8, 
        fg="black",
        font=('arial', 20, 'bold'),
        text="0",
        command=lambda:butonClick(0),
        bg="silver"
        ).grid(row=4, column=0)
    button_character = Button(
        root, 
        padx=30, 
        bd=8, 
        fg="black",
        font=('arial', 20, 'bold'),
        text=".",
        command=lambda:butonClick("."),
        bg="silver"
    ).grid(row=4, column=1)
    button_divide = Button(
        root, 
        padx=30, 
        bd=8, 
        fg="black",
        font=('arial', 20, 'bold'),
        text="/",
        command=lambda:butonClick("/"),
        bg="silver"
    ).grid(row=4, column=2)
    button_equal = Button(
        root, 
        padx=30, 
        bd=8, 
        fg="black",
        font=('arial', 20, 'bold'),
        text="=",
        command=lambda:buttonEquals(),
        bg="silver"
    ).grid(row=4, column=3)
    ##############################################################
    button_clear = Button(
        root, 
        padx=30, 
        bd=8, 
        fg="black",
        font=('arial', 20, 'bold'),
        text="C",
        command=lambda:buttonClear(),
        bg="silver",
        width=23
    ).grid(row=5, columnspan=12)

    root.mainloop()





    # columnspan=4: 1 ô mở rộng ra 4 cột
    # bd: border