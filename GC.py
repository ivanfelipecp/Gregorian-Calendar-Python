class GregorianCalendar():
    # Variables auxiliares
    diaMeses = [31,28,31,30,31,30,31,31,30,31,30,31]
    dias = ["domingo","lunes","martes","miercoles","jueves","viernes","sabado"]
    a = 0
    m = 1
    d = 2
    error = "error con la fecha"

    # Verifica si un año es bisiesto
    def bisiesto(self,a):
        if type(a)!= int:
            return False
        flag = (a%4==0 and a%100!=0) or (a%100==4)
        if flag:
            self.diaMeses[1] = 29
        return flag

    # Rango de años para utilizar la formula
    def validarRangoA(self,a):
        return a >= 1700 and a <= 2199

    # Valida que sea el año sea un tipo válido y en el rango
    def validarA(self,a):
        self.bisiesto(a)
        flag = True
        if not self.validarRangoA(a):
            flag = False

        return flag

    # Valida el mes
    def validarM(self,m):
        return (m >= 1) and (m<=12)

    # Valida el día
    def validarD(self,m,d):
        cant = self.diaMeses[m-1]
        return (d>=1) and (d<=cant)

    # Verifica que la fecha sea tupla de 3 numeros enteros, con datos validos
    def fecha_es_tupla(self,fecha):
        # Verifica que sea tupla
        flag = type(fecha) == tuple
        if not flag:
            return flag

        # Si es tupla, verifica que tenga 3 se tamaño
        flag = (len(fecha) == 3)
        if not flag:
            return flag

        # Verifica que todos sean números
        for i in fecha:
            if type(i) != int:
                flag = False
                break
        return flag

    # Usando todas las funciones anteriores de validación, verifica que la fecha sea válida        
    def fecha_es_valida(self, fecha):
        # Bandera
        flag = self.fecha_es_tupla(fecha)
        if not flag:
            return flag

        # Si llega acá, son todos números, hay que validar el dia, mes, año
        flag = self.validarA(fecha[self.a])
        flag = flag and self.validarM(fecha[self.m])
        flag = flag and self.validarD(fecha[self.m],fecha[self.d])
        return flag

    # Retorna el código del century
    def getCenturyCode(self,a):
        if a>=1700 and a<=1799:
            return 4
        elif a>=1800 and a<=1899:
            return 2
        elif a>=1900 and a<=1999:
            return 0
        elif a>=2000 and a<=2099:
            return 6
        elif a>=2100 and a<=2199:
            return 4
        elif a>=2200 and a<=2299:
            return 2
        else:
            return 0

    # Función la cual retorna el día de la semana a partir de una fecha
    # Emplea la funcion getCentury y una fórmula
    def getDiaSemana(self,fecha):
        if self.fecha_es_valida(fecha):
            y_c = (fecha[self.a] + (fecha[self.a]//4))%7
            m_c = [0,3,3,6,1,4,6,2,5,0,3,5][fecha[self.m]-1]
            c_c = self.getCenturyCode(fecha[self.a])
            l_c = 0
            if self.bisiesto(fecha[self.a]):
                l_c = 1
            return (y_c + m_c + c_c + fecha[self.d] - l_c)%7 - 1
        else:
            return self.error

    # Función que calcula el día siguiente, retorna una tupla
    def dia_siguiente(self,fecha):
        if self.fecha_es_valida(fecha):
            a = fecha[self.a]
            m = fecha[self.m]
            d = fecha[self.d]

            d +=1
            if d > self.diaMeses[m-1]:
                d = 1
                m += 1
                if m > 12:
                    m = 1
                    a += 1
            return (a,m,d)
        else:
            return self.error

    # Función auxiliar que valida si f2 es mayor que f1
    def esMayor(self,f1,f2):
        bandera = True
        if f1[self.a] > f2[self.a]:
            bandera = False
        elif f1[self.m] > f2[self.m]:
            bandera = False
        elif f1[self.d] > f2[self.d]:
            bandera = False
        return bandera
    
    # Calcula la diferencia de días
    def diferenciaDias(self, f1, f2):
        if self.fecha_es_valida(f1) and self.fecha_es_valida(f2):
            if self.esMayor(f1,f2):
                f = f1
                cont = 0
                while f != f2:
                    f = self.dia_siguiente(f)
                    cont += 1
                if f2[self.a] > f1[self.a]:
                    cont -= f2[self.a] - f1[self.a] - 1
                return cont
            else:
                return self.error
        else:
            return self.error

    # Hace el llamado de la función diferencia de dias, pero antes crea una fecha en 1 de enero
    def dias_desde_primero_enero(self,fecha):
        f1 = (fecha[self.a],1,1)
        return self.diferenciaDias(f1,fecha)

    # Usa la función getDiaSemana con el primero de enero
    def dia_primero_enero(self,a):
        #print(type(a))
        if type(a) != int or not self.validarA(a):
            return self.error
        return self.dia(self.getDiaSemana((a,1,1)))

    # Función la cual recibe un n entre 0~6 y retorna su respectivo dia, domingo 0... lunes 1...
    def dia(self,n):
        
        return self.dias[n]

    # Función aux que incrementa el dia
    def incrementarDia(self,d):
        d += 1
        if d > 6:
            d = 1
        return d

    # Funcion que imprime el calendario, usando strings, ciclos y listas
    def imprimir_3x4(self,a):
        if not self.fecha_es_valida((1,1,a)):
            return self.error
        self.bisiesto(a)
        meses1 = "{0}Enero{0} |{0}Febrero{1} |{0} Marzo{0} |{0} Abril{0} |".format(" "*11,10*" ")
        meses2 = "{0} Mayo {0}  |{0} Julio {0}  |{0} Julio {0}  |{0} Agosto {0} |".format(" "*10)
        meses3 = "{0} Setiembre  {0}|{0} Octubre {0}    |{0} Noviembre {0}  |{0} Diciembre {0}  |".format(" "*8)
        mesPrint = [meses1,meses2,meses3]
        dias = "D   L   K   M   J   V   S   | D   L   K   M   J   V   S   | D   L   K   M   J   V   S   | D   L   K   M   J   V   S   |"
        
        # Crea la matriz inicial
        meses = []
        for i in range(12):
            m = []
            for j in range(6):
                m.append([" "," "," "," "," "," "," "])
            meses.append(m)
        
        # Obtiene el dia donde inicia el año
        diaI = self.dia_primero_enero(a)     
        mes = 0

        # Asigna el numero de dia a cada mes en cada semana
        while mes < 12:
            cantD = self.diaMeses[mes]
            semana = 0
            dia = 1
            while dia <= cantD:
                if (diaI>6):
                    diaI = 0
                    semana += 1
                try:
                    meses[mes][semana][diaI] = dia
                except:
                    print(mes,semana,diaI)
                    for i in meses[mes]:
                        print(i)
                    input()
                dia += 1
                diaI += 1

            mes += 1
            if (diaI>6):
                diaI = 0

        # Imprime los primeros 4
        print(mesPrint[0])
        print(dias)
        
        for s in range(6):
            cont = 0
            for i in range(4):
                for d in range(7):
                    a = meses[i][s][d]
                    if a == " ":
                        a = " "*3
                    else:
                        l = 3 - len(str(a))
                        a = str(a) +  " "*l
                    cont += len(a)
                    print(a,end=" ")
                print("| ",end="")
            print()
        
        # Imprime los segundos 4
        print()
        print(mesPrint[1])
        print(dias)
        
        for s in range(6):
            cont = 0
            for i in range(4,8):
                for d in range(7):
                    a = meses[i][s][d]
                    if a == " ":
                        a = " "*3
                    else:
                        l = 3 - len(str(a))
                        a = str(a) +  " "*l
                    cont += len(a)
                    print(a,end=" ")
                print("| ",end="")
            print()

        # Imprime los últimos cuatro
        print()
        print(mesPrint[2])
        print(dias)
        
        for s in range(6):
            cont = 0
            for i in range(8,12):
                for d in range(7):
                    a = meses[i][s][d]
                    if a == " ":
                        a = " "*3
                    else:
                        l = 3 - len(str(a))
                        a = str(a) +  " "*l
                    cont += len(a)
                    print(a,end=" ")
                print("| ",end="")
            print()
        print()
