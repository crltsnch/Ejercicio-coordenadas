# Ejercicio-coordenadas
El enlace a mi repositorio es https://github.com/crltsnch/Ejercicio-coordenadas.git
El codigo es:

```
import math

class Punto:
    def __init__(self, coordenadaX=0, coordenadaY=0):
        self.coordenadaX=coordenadaX
        self.coordenadaY=coordenadaY
    def __str__(self):
        return "({},{})".format(self.coordenadaX, self.coordenadaY)
    
    def cuadrante(self):
        if self.coordenadaX > 0 and self.coordenadaY > 0:
            print("{} pertenece al primer cuadrante".format(self))
        elif self.coordenadaX < 0 and self.coordenadaY > 0:
            print("{} pertenece al segundo cuadrante".format(self))
        elif self.coordenadaX < 0 and self.coordenadaY < 0:
            print("{} pertenece al tercer cuadrante".format(self))
        elif self.coordenadaX > 0 and self.coordenadaY < 0:
            print("{} pertenece al cuarto cuadrante".format(self))
        elif self.coordenadaX!=0 and self.coordenadaY==0:
            print("{} esta en el eje X".format(self))
        elif self.coordenadaX==0 and self.coordenadaY!=0:
            print("{} esta en el eje Y".format(self))
        else:
            print("{} esta en el origen".format(self))

    def vector(self, p):
        print("El vector entre {} y {} es ({}, {})".format(self, p, p.coordenadaX - self.coordeandaX, p.coordenadaY - self.coordenadaY))
    
    def distancia(self, p):
        d = math.sqrt((p.coordenadaX - self.coordenadaX)**2 + (p.coordenadaY - self.coordenadaY)**2)
        print("La distancia entre los puntos {} y {} es {}".format(self, p, d))

class Rectangulo:
    def __init__(self, pInicial=Punto(), pFinal=Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal
        self.vBase = abs(self.pFinal.x - self.pInicial.x)
        self.vAltura = abs(self.pFinal.y - self.pInicial.y)
        self.vArea = abs(self.vBase * self.vAltura)

    def base(self):
        print("La base del rectangulo es {}".format(self.vBase))
    def altura(self):
        print("La altura del rectángulo es {}".format(self.vAltura))
    def area(self):
        print("La area del rectangulo es {}".format(self.vArea))

A=(3,5)
B=(8,-3)
C=(1,8)
D=(-2,-2)

A.cuadrante()
B.cuadrante()

A.vector(B)
B.vector(C)

A.distancia(B)
D.distancia(A)

R = Rectangulo(A, B)
R.base()
R.altura()
R.area()
```
