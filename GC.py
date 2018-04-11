class GregorianCalendar():
    # Variables auxiliares
    diaMeses = [31,28,31,30,31,30,31,31,30,31,30,31]
    dias = ["domingo","lunes","martes","miercoles","jueves","viernes","sabado"]
    # (dia,mes)
    feriados = [(1,1),(11,4),(1,5),(25,6),(15,8),(15,9),(25,12)]
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

        # Función que calcula el día siguiente, retorna una tupla
    def dia_anterior(self,fecha):
        if self.fecha_es_valida(fecha):
            a = fecha[self.a]
            m = fecha[self.m]
            d = fecha[self.d]

            d -=1
            if d < 1: #self.diaMeses[m-1]:
                m -= 1
                d = self.diaMeses[m]
                
                if m < 1:
                    m = 12
                    a -= 1
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
        cont = 0
        while f1 != f2:
            f1 = self.dia_siguiente(f1)
            cont += 1
            if f2[self.a] > f1[self.a]:
                cont -= f2[self.a] - f1[self.a] - 1
        return cont

    # Hace el llamado de la función diferencia de dias, pero antes crea una fecha en 1 de enero
    def dias_desde_primero_enero(self,fecha):
        f1 = (fecha[self.a],1,1)
        if not self.fecha_es_valida(f1):
            return self.error
        return self.diferenciaDias(f1,fecha)

    # Usa la función getDiaSemana con el primero de enero
    def dia_primero_enero(self,a):
        #print(type(a))
        if type(a) != int or not self.validarA(a):
            return self.error
        return self.getDiaSemana((a,1,1))

    # Función la cual recibe un n entre 0~6 y retorna su respectivo dia, domingo 0... lunes 1...
    def dia(self,n):
        if type(n) != int:
            return self.error
        return self.dias[n]

    # Función aux que incrementa el dia
    def incrementarDia(self,d):
        d += 1
        if d > 6:
            d = 1
        return d

    # Funcion que imprime el calendario, usando strings, ciclos y listas
    def imprimir_3x4(self,a):
        if not self.fecha_es_valida((a,1,1)):
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
        print("Calendario del año",a,"D.C.")
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

    # Inicio de asignación 3

    # Función auxiliar
    # Decrementa n veces una fecha
    def fecha_pasada(self,f,n):
        if type(n)!=int:
            return self.error

        if not self.fecha_es_valida(f):
            return self.error
        
        if n<0:
            return self.error

        while n > 0:
            f = self.dia_anterior(f)
            n -= 1
        return f

    
    # R7: Incrementa n veces una fecha
    def fecha_futura(self,f,n):
        if type(n)!=int:
            return self.error

        if not self.fecha_es_valida(f):
            return self.error
        
        if n<0:
            return self.error

        while n > 0:
            f = self.dia_siguiente(f)
            n -= 1
        return f

    #R8: Dias entre fechas
    def dias_entre(self,f1,f2):
        if self.fecha_es_valida(f1) and self.fecha_es_valida(f2):
            if self.esMayor(f2,f1):
                a = f1
                f1 = f2
                f2 = a
            fecha = self.diferenciaDias(f1,f2)
            return fecha
        else:
            print("aca")
            return self.error

    #R9: Dia de la semana
    def dia_semana(self,f):
        if self.fecha_es_valida(f):
            return self.getDiaSemana(f)
        else:
            return self.error

    # Funcion auxiliar para obtener la semana santa
    def getCenturyMN(self,a):
        m = 0
        n = 0
        if a>=1700 and a<=1799:
            m,n = 22,2
        elif a>=1800 and a<=1899:
            m,n = 23,3
        elif a>=1900 and a<=2099:
            m,n = 24,5
        elif a>=2100 and a<=2199:
            m,n = 24,6
        elif a>=2200 and a<=2299:
            m,n = 25,0
        if m==n==0:
            print("ceros")
        return m,n

    # Funcion auxiliar para obtener la fecha de la pascua
    def getPascua(self,a):
        m,n = self.getCenturyMN(a)
        A = a%19
        b = a%4
        c = a%7
        d = (19*A+m)%30
        e = (2*b+4*c+6*d+n)%7
        # print(a,b,c,d,e)
        fecha = ()
        f = 0
        if d+e < 10:
            f = d+e+22
            #print("cae en",d+e+22,"de marzo")
            fecha = (a,3,f)

        else:
            f = d+e-9
            if f == 26:
                f = 19
            elif f == 25 and d == 28 and e == 6 and A > 10:
                f = 18
            fecha = (a,4,f)
        return fecha

    # Funcion auxiliar, que obtiene los feriados connstantes
    # Le añade los de semana santa y los retorna
    # Esto para usarla en dias habiles
    def getFeriados(self,a):
        f = self.feriados
        pascua = self.getPascua(a)

        v = self.fecha_pasada(pascua,2)
        j = self.fecha_pasada(v,1)

        f.append((v[2],v[1]))
        f.append((j[2],j[1]))

        return f

    # auxiliar
    def isHabil(self,fecha):
        f = self.getFeriados(fecha[0])
        return not (self.dia_semana(fecha) in [0,6]) and not ((fecha[2],fecha[1]) in f)
    
    #R10: (fecha_futura_habil)
    def fecha_futura_habil(self,fecha,n):
        if type(n) != int:
            return self.error
        
        if self.fecha_es_valida(fecha) and n>=0:
            # obtiene feriados para sacar el día hábil
            
            while n > 0:
                if self.isHabil(fecha):
                    n -= 1
                    #if n == 0:
                    #    return fecha
                fecha = self.fecha_futura(fecha,1)
            return fecha
        else:
            return error

    #R11: (días_habiles_entre)
    def dias_habiles_entre(self,f1,f2):
        if self.fecha_es_valida(f1) and self.fecha_es_valida(f2):
            a = f1
            b = f2
            if self.esMayor(f2,f1):
                a = f2
                b = f1

            cont = 0
            while a != b:
                if self.isHabil(a):
                    cont += 1
                a = self.fecha_futura(a,1)
            return cont
        else:
            return self.error
