
from time import sleep
import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.maxsize(350,250)
        self.master.title("Countdown")
        self.pack(padx=250,pady=1)
        self.__create_widgets__()

    def __create_widgets__(self):
        labelFont = Font(family="Verdana",size=20)
        inputFont = Font(family="Verdana",size=12)
        buttonFont = Font(family="Verdana",size=10)

        self.inputs = tk.Frame()
        self.hours = tk.Frame(master=self.inputs)
        self.labelHours = tk.Label(master=self.hours,font=labelFont,text="HH")
        self.labelHours.pack(side="top")
        self.inputHours = tk.Text(master=self.hours,height=1,width=10,font=inputFont,spacing1=15,spacing3=15)
        self.inputHours.tag_configure("center",justify="center")
        self.inputHours.insert("1.0"," ","center")
        self.inputHours.pack(side="bottom")
        self.hours.pack(side="left",padx=5)

        self.minutes = tk.Frame(master=self.inputs)
        self.labelMinutes = tk.Label(master=self.minutes,font=labelFont,text="MM")
        self.labelMinutes.pack(side="top")
        self.inputMinutes = tk.Text(master=self.minutes,height=1,width=10,font=inputFont,spacing1=15,spacing3=15)
        self.inputMinutes.tag_configure("center",justify="center")
        self.inputMinutes.insert("1.0"," ","center")
        self.inputMinutes.pack(side="bottom")
        self.minutes.pack(side="left",padx=5)
        
        self.seconds = tk.Frame(master=self.inputs)
        self.labelSeconds = tk.Label(master=self.seconds,font=labelFont,text="SS")
        self.labelSeconds.pack(side="top")
        self.inputSeconds = tk.Text(master=self.seconds,height=1,width=10,font=inputFont,spacing1=15,spacing3=15)
        self.inputSeconds.tag_configure("center",justify="center")
        self.inputSeconds.insert("1.0"," ","center")
        self.inputSeconds.pack(side="bottom")
        self.seconds.pack(side="left",padx=5)
        
        self.inputs.pack(expand=True,pady=15)

        self.bottomCollection = tk.Frame()
        self.startButton = tk.Button(master=self.bottomCollection,height=2,width=25,font=buttonFont,text="Start Countdown",command=self.__countdown__)
        self.startButton.pack(side="top",padx=5)
        self.labelWarnings = tk.Label(master=self.bottomCollection,font=labelFont,text=" ",foreground="red")
        self.labelWarnings.pack(side="bottom",padx=5)
        self.bottomCollection.pack(side="bottom",pady=15)


    def __countdown__(self):
        try:
            s = (int(self.inputHours.get("1.0","end-1c").strip())*60 + int(self.inputMinutes.get("1.0","end-1c").strip()))*60 + int(self.inputSeconds.get("1.0","end-1c").strip())
        except:
            self.labelWarnings.configure(text="Warning: Invalid Input!")
            return

        while s > 0:
            s -= 1
            sleep(1.0)
            hours = int(s/3600)
            minutes = int((s - hours*3600)/60)
            seconds = s - hours*3600 - minutes*60
            self.__updateText__(self.inputHours," "+str(hours))
            self.__updateText__(self.inputMinutes," "+str(minutes))
            self.__updateText__(self.inputSeconds," "+str(seconds))
            self.update_idletasks()

        messagebox.showinfo(title="Countdown",message="The timer reached zero.")

    def __updateText__(self,box,text):
        box.delete("1.0","end")
        box.insert("1.0",text,"center")


root = tk.Tk()
app = Application(master=root)
app.mainloop()  

