
class Pieza:
    def __init__(self, name, width, height):
        self.name = name
        self.giros = 0
        self.pos = [-1, -1]
        self.width = width
        self.height = height
        self.area = self.width * self.height
        self.posicionar_bien()

    def imprimir(self):
        print(self.name)
        #print("  ", self.width)
        #print("  ", self.height)
        # print(self.giros)
        #print("  ", self.giros)
        print("  ", self.pos)

    def girar(self):
        self.width, self.height = self.height, self.width
        self.giros += 1

    def posicionar_bien(self):
        if max(self.width, self.height) == self.width:
            return
        else:
            self.girar()

    def resultado(self):
        if self.giros % 2 == 0:
            orientacion = 'N'
        else:
            orientacion = 'G'
        texto = self.name + ' ' + \
            str(self.pos[0]) + ' ' + str(self.pos[1]) + ' ' + orientacion

        return texto


def Establecer_data(direccion):
    file = open(direccion, 'r')
    lista = []

    line1 = file.readline().split()
    plancha = [line1[0], line1[1]]

    line2 = file.readline().split()

    for l in file.readlines():
        descripcion = l.split()
        qua = int(descripcion[3])
        num = 1
        while num <= qua:
            name = descripcion[0] + str(num)
            lista.append(Pieza(name, int(descripcion[1]), int(descripcion[2])))
            num += 1

    file.close()
    return plancha, lista


def Salida(direccion, lista):
    file_out = open(direccion, 'w')

    for i in range(len(lista)):
        line = lista[i].resultado()
        file_out.write(line)
        file_out.write('\n')

    file_out.close()


def sort_by(lista, p):
    def sort_w(obj):
        return obj.width

    def sort_n(obj):
        return obj.name

    if p == 'name':
        lista.sort(key=sort_n, reverse=True)

    elif p == 'width':
        lista.sort(key=sort_w, reverse=True)
    return lista


def compare(tabla, superficie_abajo):
    if tabla.width <= superficie_abajo[0]:
        return True
    else:
        return False


def actualizar_s_a(superficie_abajo, tabla_actual):
    if superficie_abajo[0] == tabla_actual.width:
        return False, superficie_abajo[0]
    else:
        return True, superficie_abajo[0] - tabla_actual.width


def Empecemos(d_plancha, tablas):
    n_planchas = 0
    queue = tablas[:]
    areas_libres = {}
    superficie_abajo = [tablas[0].width]
    puntos_base = [0, 0]

    def empaquetar(puntos_base, superficie_abajo):
        if len(queue):
            if compare(queue[0], superficie_abajo):
                queue[0].pos = [puntos_base[0],
                                puntos_base[1] + queue[0].height]

                al_lado, superficie_abajo[0] = actualizar_s_a(
                    superficie_abajo, queue[0])

                if al_lado:
                    puntos_base = [puntos_base[0] +
                                   queue[0].width, puntos_base[1]]
                else:
                    puntos_base = [puntos_base[0],
                                   puntos_base[1] + queue[0].height]

                queue.remove(queue[0])
            else:
                queue[0].pos = [puntos_base[0],
                                puntos_base[1] + queue[0].height]
                queue.remove(queue[0])

            empaquetar(puntos_base, superficie_abajo)

    empaquetar(puntos_base, superficie_abajo)


def main():
    direc_in = "/home/joaquin/Documents/p_python/TP_Complejidad/entrada"
    direc_out = "/home/joaquin/Documents/p_python/TP_Complejidad/salida"

    d_plancha, tablas = Establecer_data(direc_in)
    tablas = sort_by(tablas, 'width')

    Empecemos(d_plancha, tablas)

    tablas = sort_by(tablas, 'name')

    tablas[0].resultado()
    Salida(direc_out, tablas)
    # for i in range(len(tablas)):
    #    tablas[i].imprimir()


main()
