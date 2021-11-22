from abc import ABC,abstractmethod #here abc is a module called abstract base classes because python by default doesnt support  data abstration 


class shape(ABC):
  
       
    @abstractmethod #here it declares the abstract decorator bcoz of which any class which is inheriting the shape class  must define printarea  function or else programm will not run 
    def printarea(self):
        return 0


class rectangle(shape):
    type="rectangle"
    sides=4
    def __init__(self):
        self.length=6
        self.breadth=7
    def printarea(self):
        return self.length* self.breadth


rect1= rectangle()
print(rect1.printarea())

    
