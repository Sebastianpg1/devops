
from abc import ABC 

class Absnumeros(ABC):
    
    #@abstractcmethod
    def print_numeros(self):
        pass
    
class racionales(Absnumeros):
    
    def __init__(self,n):
        self.n = n
        
    def print_numeros(self):
        print ("El numero raacional es: ", self.n)
        print ("El numero en forma de fraccion es: ", self.n.as_integer_ratio())
        
        

    