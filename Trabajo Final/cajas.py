import heapq as hq
import math


class caja():
    def __init__(self, name, height, widht, longg):
        self.name = name
        self.alto = height
        self.ancho = widht
        self.largo = longg
        self.vol = self.alto * self.ancho * self.largo
        self.container = -1
        self.pos = [-1, -1, -1]
        self.orientacion = -1
        self.det_orientacion()

    def det_orientacion(self):
        if self.largo >= self.ancho and self.ancho >= self.alto:
            self.orientacion = 1
        if self.largo >= self.alto and self.alto > self.ancho:
            self.orientacion = 3
        if self.ancho >= self.largo and self.largo >= self.alto:
            self.orientacion = 2
        if self.ancho >= self.alto and self.alto > self.largo:
            self.orientacion = 4
        if self.alto >= self.largo and self.largo >= self.ancho:
            self.orientacion = 5
        if self.alto >= self.ancho and self.ancho > self.largo:
            self.orientacion = 6

    def posicionar(self, o):
        valores = [self.alto, self.ancho, self.largo]
        valores.sort()
        if o == 1:
            self.alto = valores[0]
            self.ancho = valores[1]
            self.largo = valores[2]
        elif o == 2:
            self.alto = valores[0]
            self.ancho = valores[2]
            self.largo = valores[1]
        elif o == 3:
            self.alto = valores[1]
            self.ancho = valores[0]
            self.largo = valores[2]
        elif o == 4:
            self.alto = valores[1]
            self.ancho = valores[2]
            self.largo = valores[0]
        elif o == 5:
            self.alto = valores[2]
            self.ancho = valores[0]
            self.largo = valores[1]
        elif o == 6:
            self.alto = valores[2]
            self.ancho = valores[1]
            self.largo = valores[0]

        return self.det_orientacion()

    def mostrar(self):
        print(self.name, ":", self.alto, self.ancho, self.largo, "----", self.orientacion)
        # print(self.pos)
        # print(self.orientacion)

    def __lt__(self, other):
        return self.alto > other.alto


if __name__ == "__main__":
    piezas = []

    hq.heappush(piezas, caja('A', 3, 1, 2))
    hq.heappush(piezas, caja('C', 1, 1, 2))
    hq.heappush(piezas, caja('B', 2, 2, 2))

    for i in range(len(piezas)):
        hq.heappop(piezas).mostrar()
