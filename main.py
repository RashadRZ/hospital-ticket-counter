from tkinter import *
from PIL import ImageTk, Image

# Queue
queue = []
queue_number = 1


# UI functions
def call_counter1():
    if len(queue) != 0:
        call = queue.pop(0)
        counter1.configure(text=call)
        show_next()


def call_counter2():
    if len(queue) != 0:
        call = queue.pop(0)
        counter2.configure(text=call)
        show_next()


def show_next():
    if len(queue) != 0:
        next_queue.configure(text=f'{queue[0]}')
    else:
        next_queue.configure(text='')


def take_ticket():
    global queue_number
    queue.append(f'{queue_number:03d}')
    queue_number += 1
    show_next()


# window setup
root = Tk()
root.title('Health Care')
root.iconbitmap('images/hospital.ico')

app_width = 1280
app_height = 720

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
root.resizable(False, False)
root.configure(bg='white')

# UI widget
top_frame = Frame(root, bg='white')
header_label = Label(top_frame, text='IOSEFKA\'S CLINIC', font=('Arial', 28, 'bold'), bg='white')
my_image = ImageTk.PhotoImage(Image.open('images/hospital.png'))
header_image = Label(top_frame, image=my_image, bg='white')

middle_frame = Frame(root, bg='white')
counter1_label = Label(middle_frame, text='TICKET COUNTER 1', font=('Arial', 18, 'bold'), bg='white', height=2)
counter1 = Button(middle_frame, command=call_counter1, text='', font=('Arial', 26, 'bold'), bg='black', fg='white', borderwidth=0, width=16, height=4)

counter2_label = Label(middle_frame, text='TICKET COUNTER 2', font=('Arial', 18, 'bold'), bg='white', height=2)
counter2 = Button(middle_frame, command=call_counter2, text='', font=('Arial', 26, 'bold'), bg='black', fg='white', borderwidth=0, width=16, height=4)

next_queue_label = Label(middle_frame, text='NEXT', font=('Arial', 18, 'bold'), bg='white', height=2)
next_queue = Button(middle_frame, text='', font=('Arial', 26, 'bold'), bg='white', fg='black', highlightthickness=1, highlightbackground='black', highlightcolor='black', borderwidth=0, width=16, height=4, default='active')

bottom_frame = Frame(root, bg='white')
take_ticket_button = Button(bottom_frame, command=take_ticket, text='TAKE TICKET', font=('Arial', 18, 'bold'), bg='#E20016', fg='white', borderwidth=0, width=11)

# UI positioning
top_frame.pack(pady=50)
header_label.grid(row=0, column=0)
header_image.grid(row=0, column=1)

middle_frame.pack(pady=50)
counter1_label.grid(row=0, column=0)
counter1.grid(row=1, column=0, padx=30)

counter2_label.grid(row=0, column=1)
counter2.grid(row=1, column=1, padx=30)

next_queue_label.grid(row=0, column=2)
next_queue.grid(row=1, column=2, padx=30)

bottom_frame.pack(pady=50)
take_ticket_button.grid(row=0, column=0, padx=10, pady=10)

# run
root.mainloop()
