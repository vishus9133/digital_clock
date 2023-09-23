from tkinter import Tk, Label

window = Tk()
window.title("Digital CLock")
window.geometry("600x300")
window.configure(bg="darkgreen")

label = Label(window, text="Hello!", font=("Arial Black",78,"bold"), bg="darkgreen", fg="white")
label.pack(pady=100)

window.mainloop() 