from tkinter import *
from PIL import ImageTk, Image

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

# UI component
top_frame = Frame(root, bg='white')
header_label = Label(top_frame, text='HEALTH CARE', font=('Arial', 28, 'bold'), bg='white')
my_image = ImageTk.PhotoImage(Image.open('images/hospital.png'))
header_image = Label(top_frame, image=my_image, bg='white')

middle_frame = Frame(root, bg='white')
counter1_label = Label(middle_frame, text='TICKET COUNTER 1', font=('Arial', 18, 'bold'), bg='white', height=2)
counter1 = Button(middle_frame, text='B001', font=('Arial', 26, 'bold'), bg='black', fg='white', borderwidth=0, width=16, height=4)

counter2_label = Label(middle_frame, text='TICKET COUNTER 2', font=('Arial', 18, 'bold'), bg='white', height=2)
counter2 = Button(middle_frame, text='B002', font=('Arial', 26, 'bold'), bg='black', fg='white', borderwidth=0, width=16, height=4)

next_queue_label = Label(middle_frame, text='NEXT', font=('Arial', 18, 'bold'), bg='white', height=2)
next_queue = Button(middle_frame, text='A001', font=('Arial', 26, 'bold'), bg='white', fg='black', highlightthickness=1, highlightbackground='black', highlightcolor='black', borderwidth=0, width=16, height=4, default='active')
next_queue.configure()

bottom_frame = Frame(root, bg='white')
priority = Button(bottom_frame, text='PRIORITY', font=('Arial', 18, 'bold'), bg='#E20016', fg='white', borderwidth=0, width=11)
regular = Button(bottom_frame, text='REGULAR', font=('Arial', 18, 'bold'), bg='white', fg='black', highlightthickness=1, highlightbackground='#E20016', highlightcolor='#E20016', borderwidth=0, width=11, default='active')

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
priority.grid(row=0, column=0, padx=10, pady=10)
regular.grid(row=0, column=1, padx=10, pady=10)

# run
root.mainloop()
