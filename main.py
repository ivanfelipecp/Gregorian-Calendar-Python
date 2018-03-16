class GregorianCalendar():
    fecha = ()
    diaMeses = [31,28,31,30,31,30,31,31,30,31,30,31]
    a = 0
    m = 1
    d = 2
    error = "error con la fecha"

    def validarBisiesto(self,a):
        flag = (a%4==0) and (a%400==0)
        if flag:
            self.diaMeses[1] = 29
        return flag
    def validarRangoA(self,a):
        return a >= 1700 and a <= 2199
    
    def validarA(self,a):
        flag = False
        if type(a) != int:
            return flag

        self.validarBisiesto(a)
        flag = True
        if not self.validarRangoA(a):
            flag = False

        return flag

    def validarM(self,m):
        return (m >= 1) and (m<=12)

    def validarD(self,m,d):
        cant = self.diaMeses[m-1]
        return (d>=1) and (d<=cant)

    def validarFechaTupla(self,fecha):
        # Verifica que sea tupla
        flag = type(fecha) == tuple
        if not flag:
            return flag

        # Si es tupla, verifica que tenga 3 se tamaño
        flag = (len(fecha) == 3)
        if not flag:
            return flag

        # Verifica que todos sean úmeros
        for i in fecha:
            if type(i) != int:
                flag = False
                break
        return flag
        
    def validarFecha(self, fecha):
        # Bandera
        flag = self.validarFechaTupla(fecha)
        if not flag:
            return flag

        # Si llega acá, son todos números, hay que validar el dia, mes, año
        flag = self.validarA(fecha[self.a])
        flag = flag and self.validarM(fecha[self.m])
        flag = flag and self.validarD(fecha[self.m],fecha[self.d])
        return flag

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
        
    def getDiaSemana(self,fecha):
        if self.validarFecha(fecha):
            y_c = (fecha[self.a] + (fecha[self.a]//4))%7
            m_c = [0,3,3,6,1,4,6,2,5,0,3,5][fecha[self.m]-1]
            c_c = self.getCenturyCode(fecha[self.a])
            l_c = 0
            if self.validarBisiesto(fecha[self.a]):
                l_c = 1
            return (y_c + m_c + c_c + fecha[self.d] - l_c)%7 - 1
        else:
            return self.error
    def diaSiguiente(self,fecha):
        if self.validarFecha(fecha):
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

    def esMayor(self,f1,f2):
        bandera = True
        if f1[self.a] > f2[self.a]:
            bandera = False
        elif f1[self.m] > f2[self.m]:
            bandera = False
        elif f1[self.d] > f2[self.d]:
            bandera = False
        return bandera
    def diferenciaDias(self, f1, f2):
        if self.validarFecha(f1) and self.validarFecha(f2):
            if self.esMayor(f1,f2):
                f = f1
                cont = 0
                while f != f2:
                    f = a.diaSiguiente(f)
                    cont += 1
                if f2[self.a] > f1[self.a]:
                    cont -= f2[self.a] - f1[self.a] - 1
                return cont
            else:
                return self.error
        else:
            return self.error
    def diasDesdePrimeroEnero(self,fecha):
        f1 = (fecha[self.a],1,1)
        return self.diferenciaDias(f1,fecha)
    def diaPrimeroEnero(self,a):
        return self.getDiaSemana((a,1,1))
    def dia(self,n):
        dias = ["domingo","lunes","martes","miercoles","jueves","viernes","sabado"]
        return dias[n]
    def incrementarDia(self,d):
        d += 1
        if d > 6:
            d = 1
        return d
    def imprimirA(self,a):
        """if not self.validarFecha((1,1,a)):
            return self.error"""
        self.validarBisiesto(a)
        meses1 = "{0} Enero {0}|{0} Febrero {0}|{0} Marzo {0}  |{0} Abril {0}  |".format(" "*10)
        meses2 = "{0} Mayo {0} |{0} Julio {0}  |{0} Julio {0}  |{0} Agosto {0} |".format(" "*10)
        meses3 = "{0} Setiembre {0}|{0} Octubre {0}    |{0} Noviembre {0}  |{0} Diciembre {0}  |".format(" "*8)
        mesPrint = [meses1,meses2,meses3]
        dias = "D   L   K   M   J   V   S  |" +"  D   L   K   M   J   V   S  |"*3
        
        meses = []
        for i in range(12):
            m = []
            for j in range(6):
                m.append([" "," "," "," "," "," "," "])
            meses.append(m)
        
        diaI = self.diaPrimeroEnero(a)     
        mes = 0

        #for i in meses[0]:
        #    print(i)

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

            """print("Mes #",mes)
            for i in meses[mes]:
                print(i)"""
            mes += 1
            if (diaI>6):
                diaI = 0

        #for i in range(3):
        print(mesPrint[0])
        print(dias)
        for s in range(1):
            for i in range(4):
                for d in range(7):
                    a = meses[i][s][d]
                    if a == " ":
                        a = " "*3
                    print(a,end=" ")
                print(" | ",end="")
            print()
            
            
        
        
a = GregorianCalendar()
a.imprimirA(2018)

#f1 = (2018,11,28)
#print(a.diasDesdePrimeroEnero(f1))

#print(a.imprimirA(2018))
