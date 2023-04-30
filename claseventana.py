#Clase ventana

class Ventana:
    __titulo:str
    __alto:int
    __ancho:int
    __x:int
    __y:int

    def __init__(self,titulo,alto = 0,ancho = 0, x = 0, y = 0):
        self.__titulo = titulo
        self.__alto = alto
        self.__ancho = ancho
        self.__x = x
        self.__y = y
    
    def getTitulo(self):
        return self.__titulo
    
    def alto(self):
        return self.__alto
    
    def ancho(self):
        return self.__ancho
    
    def mostrar(self):
        return print(f"Ventana:{self.__titulo} | Alto: {self.__alto} | Ancho: {self.__ancho} | Posicion(X:{self.__x} Y:{self.__y})")
    
    def moverDerecha(self, distancia):
        self.__x += distancia
    
    def moverIzquierda(self, distancia):
        self.__x -= distancia
    
    def bajar(self, distancia):
        self.__y += distancia
    
    def subir(self, distancia):
        self.__y -= distancia