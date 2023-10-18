from tkinter import *

# windows
window = Tk()
window.title("BDI calculator")
window.minsize(width=500, height=400)
window.config(padx=20,pady=20)

# label
my_label1 = Label(text="BDI")
my_label1.config(bg="black")
my_label1.config(fg="white")
my_label1.config(padx=10, pady=10)
my_label1.pack()

# weight
my_label2 = Label(text="Enter Your Weight(kg)")
my_label2.config(padx=10, pady=10)
my_label2.pack()

# weight entry
weight_entry = Entry(width=20)
weight_entry.pack()
weight_entry.focus()

# height
my_label3 = Label(text="Enter Your height(cm)")
my_label3.config(padx=10, pady=10)
my_label3.pack()

# height entry
height_entry = Entry(width=20)
height_entry.pack()




#button
def button_click():

    testcases= [weight_entry.get(), height_entry.get()]
    h=0
    for case in testcases:

        if case.isdigit():
           h=1
        else:
           h=0
    if h==0:
        my_label = Label(text="PLEASE ENTER THE NUMBER", )
        my_label.config(bg="red")
        my_label.config(fg="white", )
        my_label.config(padx=10, pady=10)
        my_label.pack()
    else:
        height2 = int(height_entry.get()) * int(height_entry.get())
        BMIfirst = int(weight_entry.get()) / height2
        BMI= BMIfirst*10000
        BMI=round(BMI,2)

        if BMI < 18:
            my_label = Label(text=f"very low. You are a very weak human {BMI}", )
            my_label.config(bg="black")
            my_label.config(fg="white", )
            my_label.config(padx=10, pady=10)
            my_label.pack()
        elif 18 <= BMI <25 :
            my_label = Label(text=f'low. You are not a weak human {BMI}'  )
            my_label.config(bg="black")
            my_label.config(fg="light green", )
            my_label.config(padx=10, pady=10)
            my_label.pack()
        elif 25 <= BMI < 30:
            my_label = Label(text=f'normal. You are a normal human {BMI}')
            my_label.config(bg="black")
            my_label.config(fg="green", )
            my_label.config(padx=10, pady=10)
            my_label.pack()
        elif 30 <= BMI < 40:
            my_label = Label(text=f'high. You are a some fat human {BMI}')
            my_label.config(bg="black")
            my_label.config(fg="dark green", )
            my_label.config(padx=10, pady=10)
            my_label.pack()
        elif 40 <= BMI:
            my_label = Label(text=f'very high. You are a very fat human {BMI}')
            my_label.config(bg="black")
            my_label.config(fg="red", )
            my_label.config(padx=10, pady=10)
            my_label.pack()


my_button = Button(text="calculator", command=button_click)
my_button.config(padx=10,pady=5)
my_button.pack()


window.mainloop()