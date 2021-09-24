from tkinter import *
import threading
import time
 
 
def chargementparralele():
    time.sleep(3)
    texte2=Label(fenetre,text="test2")
    texte2.pack()  
    time.sleep(3)
    texte3=Label(fenetre,text="test3")
    texte3.pack()  
 
t = threading.Thread(target=chargementparralele)
fenetre=Tk()                           
texte=Label(fenetre,text="test")
texte.pack()        
t.start()
 
fenetre.mainloop()
    

