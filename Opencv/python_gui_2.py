from tkinter import *
m = 0
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master=master
        self.init_window()
        self.total = 0

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        quitButton=Button(self,text="Quit",command=self.client_exit)
        quitButton.place(x=0,y=100)

        button = Button(root, text="print", command=self.number_print)
        button.place(x=0, y=0)

    def client_exit(self):
        exit()

    def number_print(self):
        self.total += 1
        print(self.total)
root=Tk()
root.geometry("400x300")
app=Window(root)
root.mainloop()