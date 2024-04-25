import tkinter as tk 

root =tk.Tk()

frameKu = tk.Frame(root, bg="blue")
frameKu.place(relwidth=0.8, relheight=0.8)

tombolKu = tk.Button(frameKu, text="tes Tombol", bg="grey", fg="red")
tombolKu.pack()

entryKu = tk.Entry(frameKu, bg="green")
entryKu.pack()

root.mainloop()