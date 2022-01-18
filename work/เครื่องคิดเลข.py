import tkinter as tk

root = tk.Tk()
root.title('เครื่องคิดเลข')
root.option_add('*font', 'angsana 30')


def clear():
    global expression
    global label_show
    result = '0'
    expression = ''
    label_show.set(result)


def press(number):
    global expression
    global label_show
    expression = expression + number
    label_show.set(expression)


def equal():
    try:
        global expression
        global label_show
        result = str(eval(expression))
        label_show.set(result)
    except:
        result = 'ERROR'
        expression = ''
    label_show.set(result)


label_show = tk.StringVar()
expression = ''
label_show.set(expression)
label_show.set(0)

label = tk.Label(root, textvariable=label_show).grid(row=0, column=0, columnspan=4, sticky='news')

button = tk.Button(root, text='CLEAR', command=clear).grid(row=1, column=0, columnspan=4 ,sticky='news')

button = tk.Button(root, text='7', command=lambda: press('7')).grid(row=2, column=0, sticky='news')
button = tk.Button(root, text='8', command=lambda: press('8')).grid(row=2, column=1, sticky='news')
button = tk.Button(root, text='9', command=lambda: press('9')).grid(row=2, column=2, sticky='news')
button = tk.Button(root, text='/', command=lambda: press('/')).grid(row=2, column=3, sticky='news')

button = tk.Button(root, text='4', command=lambda: press('4')).grid(row=3, column=0, sticky='news')
button = tk.Button(root, text='5', command=lambda: press('5')).grid(row=3, column=1, sticky='news')
button = tk.Button(root, text='6', command=lambda: press('6')).grid(row=3, column=2, sticky='news')
button = tk.Button(root, text='*', command=lambda: press('*')).grid(row=3, column=3, sticky='news')

button = tk.Button(root, text='1', command=lambda: press('1')).grid(row=4, column=0, sticky='news')
button = tk.Button(root, text='2', command=lambda: press('2')).grid(row=4, column=1, sticky='news')
button = tk.Button(root, text='3', command=lambda: press('3')).grid(row=4, column=2, sticky='news')
button = tk.Button(root, text='-', command=lambda: press('-')).grid(row=4, column=3, sticky='news')

button = tk.Button(root, text='.', command=lambda: press('.')).grid(row=5, column=0, sticky='news')
button = tk.Button(root, text='0', command=lambda: press('0')).grid(row=5, column=1, columnspan=2,sticky='news')
button = tk.Button(root, text='+', command=lambda: press('+')).grid(row=5, column=3, sticky='news')

button = tk.Button(root, text='=', command=equal).grid(row=6, column=0, columnspan=4, sticky='news')

root.mainloop()
