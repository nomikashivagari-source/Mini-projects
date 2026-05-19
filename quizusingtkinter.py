import tkinter as tk

root = tk.Tk()

root.geometry("400x300")
canvas= tk.Canvas(root, width=400, height=100)
canvas.pack()

question1 =tk.Label(canvas , text="The number of edges from the root to the node is called of the tree?").pack(pady = 10)

choice = tk.StringVar()
choice.set(2)

rb1 = tk.Radiobutton(canvas, text="Height", variable=choice, value=1)
rb2 = tk.Radiobutton(canvas, text="Depth", variable=choice, value=2)
rb3 = tk.Radiobutton(canvas, text="Length", variable=choice, value=3)    
rb4 = tk.Radiobutton(canvas, text="Width", variable=choice, value=4)

rb1.pack()
rb2.pack()
rb3.pack()
rb4.pack()

prev_btn = tk.Button(canvas,text="Previous", width=10)
prev_btn.pack(side="left", padx=20)

next_btn = tk.Button(canvas, text="Next", width=10)
next_btn.pack(side="right", padx=20)

submit_btn = tk.Button(canvas, text="Submit", width=20)
submit_btn.pack()


root.mainloop()