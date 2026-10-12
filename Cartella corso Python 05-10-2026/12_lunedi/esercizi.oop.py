#esercizio 1
class Punto:



    x=int(input())
    y=int(input())
    dx=int(input())
    dy=int(input())

    class Punto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def muovi(self, dx, dy):
             self.x += dx
             self.y += dy

    def distanza_da_origine(self):
         return (self.x**2 + self.y**2) ** 0.5

    

p = Punto(3, 4)
print("Distanza:", p.distanza_da_origine())  # Stampa 5.0

p.muovi(1, 1)
print(f"Nuove coordinate: x={p.x}, y={p.y}")

    



        