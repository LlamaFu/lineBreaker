
from tkinter import font
import tkinter as tk

class TextWin(tk.Text):
    ##Displays each loTg entry
    ##User can click log to edit lines
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self,*args,**kwargs)
        startFont = font.Font(family="Courier New",size=11)
        self.configure(width=30,height=15,font=startFont)


def breakLines(subText):
    pass


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.infoMess = tk.StringVar()
        labStartFont = font.Font(family="Courier New",size=12)
        self.infoMess.set('Copy text to BreakLines')
        self.textWin = TextWin(self)
        self.infoLab = tk.Label(self, textvariable=self.infoMess, font=labStartFont)

        self.breakBut = tk.Button(self, text="BREAK LINES", command=self.doSub,font=labStartFont)
        self.infoLab.pack()
        self.breakBut.pack()
        self.textWin.pack(side = 'left',fill='both', expand=2)
        self.breakBut.pack(side = 'bottom', pady=5)

    def doSub(self, event=None):
        endFont = font.Font(family="Courier New",size=12)
        self.input = self.textWin.get("1.0","end")
        self.exp = self.input.strip()
        self.exp = self.input.split('\n')
        s = ''
        countLines = 0
        for i in self.exp:
            s = s+i+' '
            countLines +=1
        while s[-1] == ' ':
            s = s[:-1]
        self.export = s
        #app.clipboard_clear()
        app.clipboard_append(s)
        print('after clipboard')
        self.textWin.delete("1.0","end")
        self.textWin.configure(width=30,height=15,font=endFont)
        #self.textWin.insert("1.0",str(countLines)+"LINES BROKEN! Coppied to Clipboard")
        self.infoMess.set(str(countLines)+" LINES BROKEN & Coppied Clipboard")
        self.update_idletasks()
        #print(self.export)








if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
