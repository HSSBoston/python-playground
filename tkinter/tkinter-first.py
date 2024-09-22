import tkinterweb
import tkinter


def load_website():
    frame.load_website(entry.get())


root = tkinter.Tk()
root.title('MiniBrowser')

tkinter.Label(master=root, text='> Browse some website :D <').pack()

entry = tkinter.Entry(master=root)
entry.pack()

button = tkinter.Button(master=root, text='Go!', command=load_website)
button.pack()

frame = tkinterweb.HtmlFrame(master=root)
frame.pack()

root.mainloop()
