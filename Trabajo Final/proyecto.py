import archivos
import heapq as hq


def crear_cont(cont, a_punt):
    a_punt.append({cont.vol: [0, 0, 0]})


def verificar_dimensiones(cont, caja, punto):
    capx = cont.ancho - punto[0]
    capy = cont.largo - punto[1]
    capz = cont.alto - punto[2]
    for i in range(5):
        if caja.alto <= capz and caja.ancho <= capx and caja.largo <= capy:
            return True
        else:
            caja.posicionar(i+1)

    return False


def actualizar_volumen_disponible(cont, caja, punto):
    np_alto = [punto[0], punto[1], punto[2] + caja.alto]
    np_ancho = [punto[0] + caja.ancho, punto[1], punto[2]]
    np_largo = [punto[0], punto[1] + caja.largo, punto[2]]

    for i in range(3):
        if i == 0:
            n_alto = cont.alto - np_alto[2]
            n_ancho = cont.ancho - np_alto[0]
            n_largo = cont.largo - np_alto[1]

            n_vol = n_alto*n_ancho*n_largo
            yield {n_vol: np_alto}
        if i == 1:
            n_alto = cont.alto - np_alto[2]
            n_ancho = cont.ancho - np_alto[0]
            n_largo = cont.largo - np_alto[1]

            n_vol = n_alto*n_ancho*n_largo
            yield {n_vol: np_alto}
        if i == 2:
            n_alto = cont.alto - np_alto[2]
            n_ancho = cont.ancho - np_alto[0]
            n_largo = cont.largo - np_alto[1]

            n_vol = n_alto*n_ancho*n_largo
            yield {n_vol: np_alto}


def acomodar(container, heap):              #O(n*c*k)
    a_punt = []
    prioridad = []

    crear_cont(container, a_punt)

    while heap or prioridad:        #O(n)  n->numero de cajas
        colocado = False

        if prioridad:
            c_actual = hq.heappop(prioridad)
        else:
            c_actual = hq.heappop(heap)

        for i in range(len(a_punt)):                #O(c)  c->numero de contenedores
            keys = list(a_punt[i].keys())           #O(k)  k->numero puntos de referencia

            for j in range(len(keys)):

                if c_actual.vol == keys[j] and verificar_dimensiones(container, c_actual, a_punt[i][c_actual.vol]):
                    c_actual.pos = a_punt[i][c_actual.vol]
                    c_actual.container = i + 1
                    ###################################################
                    for p in actualizar_volumen_disponible(container, c_actual, a_punt[i][c_actual.vol]):
                        a_punt[i].update(p)
                    del a_punt[i][c_actual.vol]

                    colocado = True
                    break

                else:
                    if c_actual.vol < keys[j] and verificar_dimensiones(container, c_actual, a_punt[i][keys[j]]):
                        c_actual.pos = a_punt[i][keys[j]]
                        c_actual.container = i + 1
                       ###################################################
                        for p in actualizar_volumen_disponible(container, c_actual, a_punt[i][keys[j]]):
                            a_punt[i].update(p)
                        del a_punt[i][keys[j]]

                        colocado = True
                        break

            if colocado:
                break  # break del for de contenedores

        if not colocado:
            crear_cont(container, a_punt)
            hq.heappush(prioridad, c_actual)

    return len(a_punt)


def main():
    archivos.crear("G:\TF Complejidad\in.txt")
    c, h = archivos.leer("G:\TF Complejidad\in.txt")

    arr = h.copy()
    n_connt = acomodar(c, h)

    archivos.salida("G:\TF Complejidad\out.txt", n_connt, c, arr)


if __name__ == '__main__':
    main()
