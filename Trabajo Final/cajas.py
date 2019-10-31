import heapq


class caja():
    def __init__(self, name, height, widht, longg):
        self.name = name
        self.alto = height
        self.ancho = widht
        self.largo = longg
        self.pos = [-1, -1, -1]
        self.orientacion = 0

    def det_orientacion(self):
        if self.largo >= self.ancho and self.ancho >= self.alto:
            return 1
        if self.largo >= self.alto and self.alto > self.ancho:
            return 3
        if self.ancho >= self.largo and self.largo >= self.alto:
            return 2
        if self.ancho >= self.alto and self.alto > self.largo:
            return 4
        if self.alto >= self.largo and self.largo >= self.ancho:
            return 5
        if self.alto >= self.ancho and self.ancho > self.largo:
            return 6

    def posicionar_1(self):
        mayor = 99999
        medio = 99999
        menor = 99999

    def mostrar(self):
        print(self.name)
        # print(self.alto)
        # print(self.ancho)
        # print(self.largo)
        # print(self.pos)
        # print(self.orientacion)

    def __lt__(self, other):
        return self.alto < other.alto


if __name__ == "__main__":
    piezas = []

    heapq.heappush(piezas, caja('A', 3, 1, 2))
    heapq.heappush(piezas, caja('C', 1, 1, 2))
    heapq.heappush(piezas, caja('B', 2, 2, 2))

    for i in range(len(piezas)):
        heapq.heappop(piezas).mostrar()
