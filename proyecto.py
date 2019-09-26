import pygame
import sys
import ctypes


class Pieza:
    def __init__(self, name, width, height):
        self.name = name
        self.giros = 0
        self.pos = [-1, -1]
        self.plancha = -1
        self.width = width
        self.height = height
        self.area = self.width * self.height
        self.posicionar_bien()

    def imprimir(self):
        print(self.name)
        # print("  ", self.width)
        # print("  ", self.height)
        # print(self.giros)
        # print("  ", self.giros)
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
    plancha = [int(line1[0]), int(line1[1])]

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


def sort_by(lista, p):
    def sort_w(obj):
        return obj.width

    def sort_n(obj):
        return obj.name

    if p == 'name':
        lista.sort(key=sort_n, reverse=False)

    elif p == 'width':
        lista.sort(key=sort_w, reverse=True)
    return lista


def entra_ta_pl(v_tabla, d_plancha):
    cont = 0
    if v_tabla > d_plancha[0]:
        cont += 1
    elif v_tabla > d_plancha[1]:
        cont += 1

    if cont == 2:
        return Fasle
    else:
        return True


def quitar_tablas_gigantes(queue, d_plancha):
    seguir = True
    while seguir:
        if queue[0].width == queue[0].height:
            if entra_ta_pl(queue[0].width, d_plancha):
                seguir = False
        else:
            eliminar = entra_ta_pl(queue[0].width, d_plancha) and entra_ta_pl(queue[0].height, d_plancha)

            if eliminar:
                queue.remove(queue[0])


"""def actualizar_p_in(pl_actual, d_plancha, tabla_actual, pun_actual, queue):
    if pun_actual[0] + tabla_actual.width < d_plancha[0] * pl_actual:
        resto_w = (d_plancha[0] * pl_actual) - (pun_actual[0] + tabla_actual.width)
        if resto_w >= queue[-1].width:
            return [pun_actual[0] + tabla_actual.width, pun_actual[1]]
        resto_h = d_plancha[1] - pun_actual[1]
        if resto_h >= queue[-1].width:
            return [pun_actual[0], pun_actual[1] + tabla_actual.height]

    return [pun_actual[0], pun_actual[1] + tabla_actual.height]"""


def actualizar_p_in(pl_actual, d_plancha, tabla_actual, pun_actual, queue):
    if pun_actual[0] + tabla_actual.width < d_plancha[0] * pl_actual:
        if len(queue) > 1:
            resto_w = (d_plancha[0] * pl_actual) - (pun_actual[0] + tabla_actual.width)
            if resto_w >= queue[1].width:
                return [pun_actual[0] + tabla_actual.width, pun_actual[1]]
            resto_h = d_plancha[1] - pun_actual[1]
            if resto_h >= queue[1].width:
                return [pun_actual[0], pun_actual[1] + tabla_actual.height]

    return [pun_actual[0], pun_actual[1] + tabla_actual.height]


def Empecemos(d_plancha, tablas):
    area_plancha = d_plancha[0] * d_plancha[1]
    n_planchas = 0
    queue = tablas[:]

    def empaquetar(area_restante, pun_inicial, pl_actual, nu_tabla):  # pl_actual = 1...n
        colocado = True
        if queue:
            if queue[nu_tabla].area <= area_restante:  # cabe la posibilidad de que entre en la tabla
                for i in range(2):
                    if queue[nu_tabla].width <= (pl_actual * d_plancha[0]) - pun_inicial[0] and queue[nu_tabla].height <= d_plancha[1] - pun_inicial[1]:
                        queue[nu_tabla].pos = [pun_inicial[0], pun_inicial[1] + queue[nu_tabla].height]
                        queue[nu_tabla].plancha = pl_actual

                        pun_inicial = actualizar_p_in(
                            pl_actual, d_plancha, queue[nu_tabla], pun_inicial, queue)

                        area_restante -= queue[nu_tabla].area

                        queue.remove(queue[nu_tabla])
                        break
                    else:
                        queue[0].girar()
                        colocado = False
            if colocado:
                if nu_tabla == len(queue):
                    return
                else:
                    if colocado:
                        empaquetar(area_restante, pun_inicial, pl_actual, nu_tabla)
            if not colocado:
                if nu_tabla + 1 == len(queue):
                    return
                else:
                    if colocado:
                        empaquetar(area_restante, pun_inicial, pl_actual, nu_tabla + 1)

        else:
            return -1

    # quitar_tablas_gigantes(queue, d_plancha)

    if tablas:
        while queue:
            empaquetar(area_plancha, [n_planchas * d_plancha[0], 0], n_planchas + 1, 0)
            n_planchas += 1
    else:
        return

    return n_planchas


def calc_desperdicio(d_plancha, planchas_totales, tablas):
    area_tablas = 0
    for i in range(len(tablas)):
        area_tablas += tablas[i].area

    area_planchas = planchas_totales * d_plancha[0] * d_plancha[1]

    area_desperdicio = area_planchas - area_tablas
    porc_desp = "{0:.2f}".format(((area_desperdicio * 100) / (area_planchas * 1.0)))

    return area_desperdicio, porc_desp


def Salida(direccion, lista, planchas_totales, d_plancha):
    file_out = open(direccion, 'w')

    a_des, por_des = calc_desperdicio(d_plancha, planchas_totales, lista)

    file_out.write("Planchas: " + str(planchas_totales) + " planchas utilizadas")
    file_out.write('\n')
    # file_out.write("Desperdicio: " + str(por_des) + ", Area: " + str(a_des) + " metros cuadrados")
    file_out.write("Desperdicio: " + str(por_des) + ", Area: " + "-" + " metros cuadrados")
    file_out.write('\n')

    for p in range(planchas_totales):
        file_out.write('\n')
        file_out.write("Plancha " + str(p + 1))
        file_out.write('\n')
        for i in range(len(lista)):
            if p + 1 == lista[i].plancha:
                line = lista[i].resultado()
                file_out.write(line)
                file_out.write('\n')

    file_out.close()


def graficos(d_plancha, planchas_totales, lista):

    pygame.init()

    s_width = 600
    s_height = 600
    screen = pygame.display.set_mode((1200, s_height))
    font = pygame.font.SysFont('Arial', 10)

    blanco = (0, 0, 0)
    negro = (255, 255, 255)
    c_rect = (125, 125, 125)
    entre = 5

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(negro)

        for p in range(planchas_totales):
            x = 25 + (p * d_plancha[0] / entre)
            y = 25
            pygame.draw.rect(screen, (100, 200, 50), (x, y, d_plancha[0] / entre, d_plancha[1] / entre), 1)

        for t in range(len(lista)):
            x = 25 + (((lista[t].plancha - 1) * d_plancha[0]) / entre) + ((lista[t].pos[0] - ((lista[t].plancha - 1) * d_plancha[0])) / entre)
            y = 25 + (d_plancha[1] / entre) - (lista[t].pos[1] / entre)
            rec = (x, y, lista[t].width / entre, lista[t].height / entre)
            pygame.draw.rect(screen, c_rect, rec, 1)

            x_text = x + lista[t].width / (entre * 2)
            y_text = y + lista[t].height / (entre * 2)
            rect_text = (x_text, y_text)

            screen.blit(font.render(lista[t].name, True, blanco, negro), rect_text)

        pygame.display.flip()


def main():
    direc_in = "/home/joaquin/Documents/p_python/TP_Complejidad/entrada"
    direc_out = "/home/joaquin/Documents/p_python/TP_Complejidad/salida"

    d_plancha, tablas = Establecer_data(direc_in)
    tablas = sort_by(tablas, 'width')

    planchas_totales = Empecemos(d_plancha, tablas)

    tablas = sort_by(tablas, 'name')

    Salida(direc_out, tablas, planchas_totales, d_plancha)

    graficos(d_plancha, planchas_totales, tablas)


main()
