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
            print('No data')
            #sys.exit(0)
        else:
            global id
            for row in data:
                print(row[0])
                print(row[1])
                id = row[0]
                if row[1] > 0:
                    print('Datos correctos')

                    from Redes2.Gui.GuiAfterAutentication import  app
                    app.mainloop()

                else:
                    print('Datos Incorrectos')
    except IOError as e:
        print('Error (0) in register Student').format(e.errno, e.strerror)
    finally:
        con_sql.close()


def mover_archivo(x,filename):
    try:
        origen = 'C:/Users/Karol/Desktop/FilesR/' + filename
        s = 'C:/Users/Karol/Desktop/quarantine/'
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

def register_quarantine(p,filename):
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
                    print('Se registro con exito en Q')
                    con_sql.close()
                    mover_archivo(p, filename)
                if re[1]==0:
                    print('No registro con exito en Q')


    except IOError as e:
        print('Error (0) en registrar el archivo en Q').format(e.errno, e.strerror)




def register_files(has,card,filename):
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
                    register_quarantine(has,filename)

    except IOError as e:
        print('Error (0) in register Files').format(e.errno, e.strerror)
    finally:
        con_sql.close()





def create_hast():
    try:
        ejemplo_dir = 'C:/Users/Karol/Desktop/FilesR/'
        contenido = os.listdir(ejemplo_dir)
        imagenes = []
        for fichero in contenido:
            if os.path.isfile(os.path.join(ejemplo_dir, fichero)) and fichero.endswith('.txt'):
                imagenes.append(fichero)
                print(imagenes)

        md5_hash = hashlib.md5()

        for x in imagenes:
            a_file = open("C:/Users/Karol/Desktop/FilesR/"+x, "rb")
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
                        register_files(digest, id, filename)
                        time.sleep(2)

                if row[1] ==1:
                    print("hast existente, se mueve a quantentena")
                    for xb in imagenes:
                        register_quarantine(digest, xb)
                        time.sleep(2)

                         #Ya existe el hash, por ende pasa a quarentena

    except IOError as e:
        print('Error (0) Error en el metodo  crear hash ....').format(e.errno, e.strerror)
    finally:
        con_sql.close()

#t=threading.Thread(target=create_hast)


def hilo():
    try:
        while True:
            create_hast()
            time.sleep(3)



    except IOError as e:
        print('Error (0) en Hilo()').format(e.errno, e.strerror)
    finally:
        print('Finalizo');


def configuracion_horario(ocurrencia,fechaIn,dia):

    if ocurrencia=='Diario':
        print("Diario")
        diario(fechaIn);


    if ocurrencia=="Semanal":
        print("Semanal")
        semanal(fechaIn,dia);

    if ocurrencia=='Mensual':
        print("Mensual")
        mensual(fechaIn,dia);

def diario(fechaIn):
   fecha_sistema=time.strftime('%Y/%m/%d %H:%M:%S')
   hora_sistema = time.strftime('H:%M:%S')

   if fechaIn<hora_sistema:
        print("Configuracion Diaria")
        hilo()
   else:
        print("El escaneo no se puede realizar, verifique las fechas.")


def semanal(fechaIn,dia):
    fecha_sistema = time.strftime('%Y/%m/%d %H:%M')
    hora_sistema=time.strftime('%H:%M')

    dia_sistema=time.strftime('%w') # me devuelve el numero del dia de la semana del sistema
    dia_system =int(dia_sistema)

    if (fechaIn <=hora_sistema or  fechaIn>=hora_sistema) and (dia_system==dia):
          print("--Configuracion Semanal--")
          print("--Se scanean todos los --", dia)
          hilo()
    else:
          print("El escaneo no se puede realizar en esas fechas -Semanal")


def mensual(fechaIn,dia):
    fecha_sistema = time.strftime('%Y/%m/%d')
    hora_sistema = time.strftime('H:%M:%S')
    dia_sistema = time.strftime('%a')
    dia_sistema = time.strftime('%w')  # me devuelve el numero del dia de la semana del sistema
    dia_system = int(dia_sistema) #parseo
    print("El proximo scaneo es el mes: Diciembre: y dia:",dia)

    if (fechaIn <=hora_sistema or  fechaIn>=hora_sistema) and (dia_system==dia):
        print("---Configuracion Mensual--")
        hilo()

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
