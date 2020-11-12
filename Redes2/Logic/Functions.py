import threading,time
import datetime

from Redes2.data.ConfigurationDB import  get_data_from_sql
from Redes2.data.ConfigurationDB import  mssql_connection
import os, sys, time, hashlib,shutil




def registerCustomers (card,password):
    try:
        query = '[Customer].[registerCustomer] ' + "'"+card+"'" + "," + "'"+password+"'"
        con_sql = mssql_connection()
        data = get_data_from_sql(query)

        if len(data) <= 0:
            print('No data')
            #sys.exit(0)
        else:
            print('Se ha registrado correctamente '+str(len(data)))
        #return 0
    except IOError as e:
        print('Error (0) in register Customer').format(e.errno, e.strerror)
    finally:
        con_sql.close()


def autentication_customers(card):
    try:
        query = '[Customer].[autentication] ' + "'"+card+"'"
        print('query'+query)
        con_sql = mssql_connection()
        data = get_data_from_sql(query)

        if len(data) <= 0:
            print('No data from Autentication')
            #sys.exit(0)
        else:
            global id
            for row in data:
                print(row[0])
                print(row[1])
                id = row[0]
                if row[1] > 0:
                    print('Datos correctos')
                    from Redes2.Gui.GuiCustomer import horario
                    horario()

                    #from Redes2.Gui.GuiAfterAutentication import  app
                    #app.mainloop()



                else:
                    print('Datos Incorrectos')
    except IOError as e:
        print('Error (0) in register Student').format(e.errno, e.strerror)
    finally:
        con_sql.close()


def mover_archivo(x,filename,origen,destino):
    try:
        origen=origen+filename
        s=destino
        #origen = 'C:/Users/Karol/Desktop/FilesR/' + filename
        #s = 'C:/Users/Karol/Desktop/quarantine/'
        if os.path.exists(origen):
            ruta = shutil.copy(origen, s)
               #  shutil.copy copia shutil.move mueve
            print('El archivo' + filename + ', con hast: ' + x + ' ha sido movido a', s)
        else:
            print('El archivo origen no existe')
    except IOError as e:
        print('Error al mover el archivo').format(e.errno, e.strerror)
    finally:
        print('XD')

def register_quarantine(p,filename,origen,destino):
    try:
        query = 'Files.register_quarantine ' + "'" + p +"',"+"'"+filename+"'"
        #query = '[Files].[register_quarantine] ' + "'" + hash + "'" + "," + "'" + filename + "'"
        con_sql = mssql_connection()
        data = get_data_from_sql(query)

        if len(data) <= 0:
            print('No data from regiter quarentena')
           # sys.exit(0)
        else:
            for re in data:
                if re[1]==1:
                    print('Se registro con exito en Quarentena')
                    con_sql.close()
                    mover_archivo(p, filename,origen,destino)
                if re[1]==0:
                    print('No registro con exito en Quarentena')


    except IOError as e:
        print('Error (0) en registrar el archivo en Q').format(e.errno, e.strerror)




def register_files(has,card,filename,orige,destino):
    try:
        query = '[FILES].register_files ' + "'" + has + "', "+str(card)+","+"'"+filename+"'"
        print(query)
        con_sql = mssql_connection()
        data = get_data_from_sql(query)

        if len(data) <= 0:
            print('No data')
            #sys.exit(0)
        else:
            for row in data:
                if row[1]==1:
                    print('Se ha registrado correctamente el archivo ')
                if row[1]==0:
                    print('Se ha registrado correctamente el archivo ')
                    register_quarantine(has,filename,orige,destino)

    except IOError as e:
        print('Error (0) in register Files').format(e.errno, e.strerror)
    finally:
        con_sql.close()





def create_hast(origen,destino):
    try:
        ejemplo_dir=origen
        #ejemplo_dir = 'C:/Users/Karol/Desktop/FilesR/'
        contenido = os.listdir(ejemplo_dir)
        imagenes = []
        for fichero in contenido:
            if os.path.isfile(os.path.join(ejemplo_dir, fichero)) and fichero.endswith('.txt'):
                imagenes.append(fichero)
                print(imagenes)

        md5_hash = hashlib.md5()

        for x in imagenes:
            a_file = open(origen+x, "rb")
            # a_file = open("C:/Users/Karol/Desktop/FilesR/"+x, "rb")
            content = a_file.read()
            md5_hash.update(content)
            digest = md5_hash.hexdigest()
            print("Hash"+digest)
            #COMPROBAR

        if a_file is None:
            print('Archivo no existe')

        for a in imagenes:
            query = '[Files].[getFiles]  ' + "'" + digest + "', " + str(id)+ ", '" +a+"'"

        con_sql = mssql_connection()
        data = get_data_from_sql(query)
        if len(data) <= 0:
            print('No hay archivos, registren uno!')

                #sys.exit(0)
        else:

            for row in data:
                if row[1] ==0:
                    print("Nuevo registro");
                        #Nuevo regisstro entrante, se registra
                    for filename in imagenes:
                        register_files(digest, id, filename,origen,destino)
                        time.sleep(2)

                if row[1] ==1:
                    print("hast existente, se mueve a quantentena")
                    for xb in imagenes:
                        register_quarantine(digest, xb,origen,destino)
                        time.sleep(2)

                         #Ya existe el hash, por ende pasa a quarentena

    except IOError as e:
        print('Error (0) Error en el metodo  crear hash ....').format(e.errno, e.strerror)
    finally:
        con_sql.close()

#t=threading.Thread(target=create_hast)


def hilo(origen,destino):
    try:
        while True:
            create_hast(origen,destino)
            time.sleep(3)



    except IOError as e:
        print('Error (0) en Hilo()').format(e.errno, e.strerror)
    finally:
        print('Finalizo');


def configuracion_horario(ocurrencia,fechaIn,dia,tipoescaneo):
    origen_dir="C:/Users/Karol/Desktop/FilesR/"
    destino_dir="C:/Users/Karol/Desktop/quarantine/"
    origen_c = "C:/"
    destino_c="C:/quarentena"


    if ocurrencia=='Diario':
        print("Diario")
        if tipoescaneo ==8: #es TOTAL
            print("Escaneo TOTAL disco C:")
            diario(fechaIn,origen_c,destino_c);
        elif tipoescaneo == 9:#solo DIR
            print("Escaneo Completo ")
            diario(fechaIn,origen_dir,destino_dir)

    if ocurrencia=="Semanal":
        print("Semanal",tipoescaneo)
        if tipoescaneo == 8:  # es TOTAL
            print("Escaneo TOTAL disco C:")
            semanal(fechaIn,dia, origen_c, destino_c);
        elif tipoescaneo == 9:  # solo DIR
            print("Escaneo Completo ")
            semanal(fechaIn,dia, origen_dir, destino_dir)


    if ocurrencia=='Mensual':
        print("Mensual")
        if tipoescaneo == 8:  # es TOTAL
            print("Escaneo TOTAL disco C:")
            mensual(fechaIn, dia, origen_c, destino_c);
        elif tipoescaneo == 9:  # solo DIR
            print("Escaneo Completo ")
            mensual(fechaIn, dia, origen_dir, destino_dir)

def diario(fechaIn,origen,destino):
   fecha_sistema=time.strftime('%Y/%m/%d %H:%M:%S')
   hora_sistema = time.strftime('H:%M:%S')

   if fechaIn<hora_sistema:
        print("Configuracion Diaria")
        hilo(origen,destino)
   else:
        print("El escaneo no se puede realizar, verifique las fechas.")


def semanal(fechaIn,dia,origen,destino):
    fecha_sistema = time.strftime('%Y/%m/%d %H:%M')
    hora_sistema=time.strftime('%H:%M')

    dia_sistema=time.strftime('%w') # me devuelve el numero del dia de la semana del sistema
    dia_system =int(dia_sistema)

    if (fechaIn <=hora_sistema or  fechaIn>=hora_sistema) and (dia_system==dia):
          print("--Configuracion Semanal--")
          print("--Se scanean todos los --", dia)
          hilo(origen,destino)
    else:
          print("El escaneo no se puede realizar en esas fechas -Semanal")


def mensual(fechaIn,dia,origen,destino):
    fecha_sistema = time.strftime('%Y/%m/%d')
    hora_sistema = time.strftime('H:%M:%S')
    dia_sistema = time.strftime('%a')
    dia_sistema = time.strftime('%w')  # me devuelve el numero del dia de la semana del sistema
    dia_system = int(dia_sistema) #parseo
    print("El proximo scaneo es el mes: Diciembre: y dia:",dia)

    if (fechaIn <=hora_sistema or  fechaIn>=hora_sistema) and (dia_system==dia):
        print("---Configuracion Mensual--")
        hilo(origen,destino)

    else:
        print("No es posible realizar el escaneo, Verifique sus fechas.")


def obtener_datos():
    try:
        query = '  [FILES].getAllFiles'
        con_sql = mssql_connection()
        data = get_data_from_sql(query)

        if len(data) <= 0:
            print('No data')
            #sys.exit(0)
        else:
            for datos in data:
                print('Nombre archivo '+datos[0])
                print('firmas'+datos[1])
                print('estado '+datos[2])
                print('cliente: jaha ')
        return data;
    except IOError as e:
        print('Error (0) in register Customer').format(e.errno, e.strerror)
    finally:
        con_sql.close()
