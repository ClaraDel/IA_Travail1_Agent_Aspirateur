from tkinter import *

  
class Table(): 
      
    def __init__(self, env, root): 
        self.root = root
        self.env = env
        self.messageCaseJew = ""
        self.messageCaseDirt = ""
        for i in range(5): 
            for j in range(5): 
                self.e = Entry(self.root, width=20) 
                self.e.grid(row=i, column=j)
        
                
    def update_draw(self):
        loop_active = True
        while loop_active:
            for i in range(5): 
                for j in range(5): 
                    if(self.env.env[i][j].jew == True):
                        self.messageCaseJew = "Bijoux"
                        if(self.env.env[i][j].dirt == True):
                            self.messageCaseDirt = "Poussière"
                    self.e.insert(END, str(self.messageCaseJew + " " + self.messageCaseDirt))
                    self.messageCaseJew = self.messageCaseDirt = ""
                
            
    def draw_env(self, root):
        #root.mainloop()
        return
    
    def close_env(self, root):
        root.quit()

                          