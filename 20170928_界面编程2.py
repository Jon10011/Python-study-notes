#coding=utf-8
from Tkinter import *
root = Tk()
root.title('Cal')
root.geometry('210x200+300+400')

def clear():
    display.set("")
def dele(n):
    display.set(str(display.get()[:-1]))
    #display.set(n)
    print n
def div(m):
    content = display.get() + m
    display.set(content)

def equal():
    try:
        con = display.get()
        res = eval(con)
        display.set(con + '=' + str(res))
    except:
        display.set('Error')
        clear()

#def main():
global display
display = StringVar()
label = Label(root,textvariable = display,relief='sunken',borderwidth=3,anchor=SE)
label.config(bg='grey',width=25,height=3)
#Label['textvariable']=display

label.grid(row=0,column=0,columnspan=4)
Button(root, text='C',fg='#EF7321',width=3,command=lambda :clear()).grid(row=1,column=0)
Button(root, text='DEL',width=3, command=lambda: dele()).grid(row=1,column=1)
Button(root, text='/',  width=3, command=lambda: div('/')).grid(row=1, column=2)
Button(root, text='*', width=3, command=lambda: div('*')).grid(row=1, column=3)
Button(root, text='7', width=3, command=lambda: dele(7)).grid(row=2, column=0)
Button(root, text='8', width=3, command=lambda: dele(8)).grid(row=2, column=1)
Button(root, text='9', width=3, command=lambda: dele(9)).grid(row=2, column=2)
Button(root, text='-', width=3, command=lambda: div('-')).grid(row=2, column=3)
Button(root, text='4', width=3, command=lambda: dele(4)).grid(row=3, column=0)
Button(root, text='5', width=3, command=lambda: dele(5)).grid(row=3, column=1)
Button(root, text='6', width=3, command=lambda: dele(6)).grid(row=3, column=2)
Button(root, text='+', width=3, command=lambda: div('+')).grid(row=3, column=3)
Button(root, text='1', width=3, command=lambda: dele(1)).grid(row=4, column=0)
Button(root, text='2', width=3, command=lambda: dele(2)).grid(row=4, column=1)
Button(root, text='3', width=3, command=lambda: dele(3)).grid(row=4, column=2)
Button(root, text='0', width=6, command=lambda: dele(0)).grid(row=5, column=0)
Button(root, text='.', width=3, command=lambda: dele('.')).grid(row=5, column=2)
Button(root, text='=', width=3, command=lambda: equal()).grid(row=5, column=3)
e = Button(root)
root.mainloop()