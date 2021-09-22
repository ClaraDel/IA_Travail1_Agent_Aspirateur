from tkinter import *

  
class Table: 
      
    def __init__(self, root, env): 
        messageCaseJew = ""
        messageCaseDirt = ""
        for i in range(5): 
            for j in range(5): 
                self.e = Entry(root, width=20) 
                self.e.grid(row=i, column=j) 
                if(env.env[i][j].jew == True):
                    messageCaseJew = "Bijoux"
                if(env.env[i][j].dirt == True):
                    messageCaseDirt = "Poussière"
                self.e.insert(END, str(messageCaseJew + " " + messageCaseDirt))
                messageCaseJew = messageCaseDirt = ""
                
# def draw:
#     env = Environnement()
#     root = Tk() 
#     t = Table(root) 
#     root.mainloop() 