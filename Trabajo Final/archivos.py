from string import ascii_lowercase
import itertools
import random
import cajas


def iter_all_strings():
    for size in itertools.count(1):
        for s in itertools.product(ascii_lowercase, repeat=size):
            yield "".join(s)


def crear(direc):
    file = open(direc, 'w')

    hb, wb, ab = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
    qf = random.randint(1, 10)

    file.write(str(hb) + " " + str(wb) + " " + str(ab))
    file.write("\n")
    file.write(str(qf))
    file.write("\n")

    for i in range(qf):
        hp, wp, ap = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
        qp = random.randint(1, 5)
        L = ""
        for s in itertools.islice(iter_all_strings(), i+1):
            L = s.upper()

        text = str(qp) + " " + L + " " + str(hp) + " " + str(wp) + " " + str(ap)
        file.write(text)
        file.write("\n")

    file.close()


def leer(direc):
    file = open(direc, 'r')

    line = file.readline().split()
    contenedor = [int(line[0]), int(line[1]), int(line[2])]
    qf = int(file.readline())
    heap = []

    for i in range(qf):
        line = file.readline().split()
        for j in range(int(line[0])):
            pieza = caja(str(line[1] + str(i+1)), int(line[2]), int(line[3]), int(line[4]))

    file.close()


if __name__ == "__main__":
    crear("/home/mrjoako/Documents/Sublime/Python/TF Complejidad/in.txt")
