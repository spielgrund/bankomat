import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("640x480")
root.title("Bankomat")
root.resizable(1,1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.columnconfigure(2, weight=1)

kontostand = 5000

#Grundlayout Grid 3x2

f1 = tk.Frame(root, width=100, height=100, bg="#ff0000")
f1.grid(column=0, row=0, )

f2 = tk.Frame(root, width=300, height=300, bg="#aa0000")
f2.grid(column=1, row=0, )

f3 = tk.Frame(root, width=100, height=100, bg="#660000")
f3.grid(column=2, row=0, )

f4 = tk.Frame(root, width=100, height=100, bg="#0000ff")
f4.grid(column=0, row=1, )

f5 = tk.Frame(root, width=100, height=100, bg="#0000aa")
f5.grid(column=1, row=1, )

f6 = tk.Frame(root, width=100, height=100, bg="#000066")
f6.grid(column=2, row=1, )

# Vier Buttons Links in Gridzelle f1

btn_left_1 = tk.Button(f1, width=10, height=2, text="Left 1")
btn_left_1.grid(column=0, row=0)

btn_left_2 = tk.Button(f1, width=10, height=2, text="Left 2")
btn_left_2.grid(column=0, row=1)

btn_left_3 = tk.Button(f1, width=10, height=2, text="Left 3")
btn_left_3.grid(column=0, row=2)

btn_left_4 = tk.Button(f1, width=10, height=2, text="Left 4")
btn_left_4.grid(column=0, row=3)

# Vier Buttons Rechts in Gridzelle f3

btn_right_1 = tk.Button(f3, width=10, height=2, text="Right 1")
btn_right_1.grid(column=0, row=0)

btn_right_2 = tk.Button(f3, width=10, height=2, text="Right 2")
btn_right_2.grid(column=0, row=1)

btn_right_3 = tk.Button(f3, width=10, height=2, text="Right 3")
btn_right_3.grid(column=0, row=2)

btn_right_4 = tk.Button(f3, width=10, height=2, text="Right 4")
btn_right_4.grid(column=0, row=3)





#Numpad Buttons in Gridzelle f5


btn_num_7 = tk.Button(f5, width=5, height=2, text=7)
btn_num_7.grid(column=0, row=0)

btn_num_8 = tk.Button(f5, width=5, height=2, text=8)
btn_num_8.grid(column=1, row=0)

btn_num_9 = tk.Button(f5, width=5, height=2, text=9)
btn_num_9.grid(column=2, row=0)

btn_num_4 = tk.Button(f5, width=5, height=2, text=4)
btn_num_4.grid(column=0, row=1)

btn_num_5 = tk.Button(f5, width=5, height=2, text=5)
btn_num_5.grid(column=1, row=1)

btn_num_6 = tk.Button(f5, width=5, height=2, text=6)
btn_num_6.grid(column=2, row=1)

btn_num_1 = tk.Button(f5, width=5, height=2, text=1)
btn_num_1.grid(column=0, row=2)

btn_num_2 = tk.Button(f5, width=5, height=2, text=2)
btn_num_2.grid(column=1, row=2)

btn_num_3 = tk.Button(f5, width=5, height=2, text=3)
btn_num_3.grid(column=2, row=2)

btn_num_0 = tk.Button(f5, width=5, height=2, text=0)
btn_num_0.grid(column=0, row=3)


#############################################################

#Text im Hauptfenster

text = tk.Text(f2, width= 25, height=10)
text.pack()
text.insert(1.0, "Kontostand: " + str(kontostand) + " €")



root.mainloop()

