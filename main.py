from tkinter import *

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
header = Label(root, text="HEALTH CARE", font=('Arial', 32, 'bold'),  height=10)

counter1_label = Label(root, text="TICKET COUNTER 1", font=('Arial', 32, 'bold'),  height=2)
counter2_label = Label(root, text="TICKET COUNTER 2", font=('Arial', 32, 'bold'),  height=2)
next_queue_label = Label(root, text="NEXT", font=('Arial', 32, 'bold'),  height=2)

counter1 = Button(root, text="B001", font=('Arial', 32, 'bold'),  width=50, height=10)
counter2 = Button(root, text="B002", font=('Arial', 32, 'bold'),  width=50, height=10)
next_queue = Button(root, text="A001", font=('Arial', 32, 'bold'),  width=50, height=10)

priority = Button(root, text="PRIORITY", font=('Arial', 32, 'bold'),  width=30, height=3)
regular = Button(root, text="REGULAR", font=('Arial', 32, 'bold'),  width=30, height=3)

# UI positioning


# run
root.mainloop()
