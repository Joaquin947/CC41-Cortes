from string import ascii_lowercase
import itertools
import random
import cajas
import heapq as hq


def iter_all_strings():
    for size in itertools.count(1):
        for s in itertools.product(ascii_lowercase, repeat=size):
            yield "".join(s)


def crear(direc):       #O(n)  n->numero de cajas
    file = open(direc, 'w')


    gt, lt = 10, 20
    hc, wc, lc = random.randint(gt, lt), random.randint(gt, lt), random.randint(gt, lt)
    qf = random.randint(gt, lt)

    file.write(str(hc) + " " + str(wc) + " " + str(lc))
    file.write("\n")
    file.write(str(qf))
    file.write("\n")

    for i in range(qf):
        hp, wp, ap = random.randint(1, int(hc)), random.randint(1, int(wc)), random.randint(1, int(lc))
        qp = random.randint(1, 5)
        L = ""
        for s in itertools.islice(iter_all_strings(), i+1):
            L = s.upper()

        text = str(qp) + " " + L + " " + str(hp) + " " + str(wp) + " " + str(ap)
        file.write(text)
        file.write("\n")

    file.close()


def leer(direc):        #O(n)  n->numero de cajas
    file = open(direc, 'r')

    line = file.readline().strip().split()
    contenedor = cajas.caja("Container", int(line[0]), int(line[1]), int(line[2]))
    qf = int(file.readline())
    heap = []

    for i in range(qf):
        line = file.readline().strip().split()
        for j in range(int(line[0])):
            pieza = cajas.caja(str(line[1]), int(line[2]), int(line[3]), int(line[4]))
            pieza.posicionar(contenedor.orientacion)
            hq.heappush(heap, pieza)

    file.close()

    return contenedor, heap


def salida(direc, numcont, contenedor, arr):        #O(n)  n->numero de cajas
    file = open(direc, 'w')

    vol_disponible = contenedor.vol*numcont
    vol_ocupado = 0
    for i in range(len(arr)):
        vol_ocupado += arr[i].vol

    porc_vol_ocupado = "{0:.2f}".format((vol_ocupado*100.0)/vol_disponible)

    def sort_by(lista):
        def sort_cont_number(obj):
            return obj.container

        def sort_name(obj):
            return obj.name

        lista.sort(key=sort_cont_number, reverse=False)
        lista.sort(key=sort_name, reverse=False)
        return lista

    arr = sort_by(arr)
    print()

    file.write("Contenedores usados: " + str(numcont) + "\n")
    file.write("Volumen disponible: " + str(vol_disponible) + "m3" + "\n")
    file.write("Volumen ocuapdo: " + str(vol_ocupado) + "m3" + "(" + str(porc_vol_ocupado) + "%)" + "\n")
    file.write("Cajas a transportar: " + str(len(arr)) + "\n")
    file.write("Contenedor\tFormato\tCoordenadas\tOrientacion\n")

    for i in range(len(arr)):
        a = str(arr[i].container)
        b = str(arr[i].name)
        c = (str(arr[i].pos[0]), str(arr[i].pos[1]), str(arr[i].pos[2]))
        d = str(arr[i].orientacion)

        file.write(a + "\t\t\t" + b + "\t\t(" + c[0] + "," + c[1] + "," + c[2] + ")\t\t" + d + "\n")


if __name__ == "__main__":
    crear("/home/mrjoako/Documents/Sublime/Python/TF Complejidad/in.txt")
    c, a = leer("/home/mrjoako/Documents/Sublime/Python/TF Complejidad/in.txt")
    salida("/home/mrjoako/Documents/Sublime/Python/TF Complejidad/out.txt", 1, c, a)
    c.mostrar()
    while a:
        x = hq.heappop(a)
        x.mostrar()
