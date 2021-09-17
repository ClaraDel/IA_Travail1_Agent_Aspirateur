
class Environnement :
    int NbrCaseSales
    
    def __init__(self ):
        self.env = []
        for i in range(5):
            l = []
            for j in range(5):
                l.append(Case(False,False, False))
            env.append(l)
    
    
        #Display the env in console
    def print_env():
        for row in self.env:
            for col in row:
                if col.jew:
                    print("J",end='')
                if col.dirt:
                    print("D",end='')
                if col.aspi:
                    print("A",end='')
                if (not(col.dirt) and not(col.jew) and not(col.aspi)):
                    print("X",end='')
                print("  ",end='')
            print('')
        print("----------")
