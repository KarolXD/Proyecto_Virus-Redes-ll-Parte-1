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
            sys.exit(0)
        else:
            print('Se ha registrado correctamente '+str(len(data)))
        #return 0
    except IOError as e:
        print('Error (0) in register Student').format(e.errno, e.strerror)
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
            sys.exit(0)
        else:
            global id
            for row in data:
                print(row[0])
                print(row[1])
                id = row[0]
                if row[1] > 0:
                    print('Datos correctos')
                    #from Redes2.Logic.socket_echo_client import socket_client
                    #socket_client()
                    from Redes2.Gui.GuiAfterAutentication import  app
                    app.mainloop()
                else:
                    print('Datos Incorrectos')
    except IOError as e:
        print('Error (0) in register Student').format(e.errno, e.strerror)
    finally:
        con_sql.close()



def register_quarantine(hash,filename):
    try:
        query = 'Files.register_quarantine ' + "'" + hash +"',"+"'"+filename+"'"
        print(query)
        con_sql = mssql_connection()
        data = get_data_from_sql(query)

        if len(data) <= 0:
            print('No data')
            sys.exit(0)
        else:
            print('Se ha registrado correctamente '+str(len(data)))

    except IOError as e:
        print('Error (0) in register Student').format(e.errno, e.strerror)
    finally:
        con_sql.close()


def register_files(has,card,filename):
    try:
        query = '[FILES].register_files ' + "'" + has + "', "+str(card)+","+"'"+filename+"'"
        print(query)
        con_sql = mssql_connection()
        data = get_data_from_sql(query)

        if len(data) <= 0:
            print('No data')
            sys.exit(0)
        else:
            print('Se ha registrado correctamente '+str(len(data)))

    except IOError as e:
        print('Error (0) in register Student').format(e.errno, e.strerror)
    finally:
        con_sql.close()


def scanner_files():
    print('scanning')
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

            #COMPROBAR
            query = '[Files].syncronization ' + "'" + digest + "', " + str(id)
            con_sql = mssql_connection()
            data = get_data_from_sql(query)
            if len(data) <= 0:
                print('No data from database')
                sys.exit(0)
            else:
                for row in data:
                    #print('filenames dangers: '+row[0])
                    ruta = os.getcwd() + os.sep #Obtiene ruta del proyecto
                    origen = 'C:/Users/Karol/Desktop/FilesR/'+row[0]
                    destino = 'C:/Users/Karol/Desktop/quarantine/'

                    if os.path.exists(origen):
                        ruta = shutil.move(origen, destino)

                        print('El archivo' +row[0]+' ha sido movido a', ruta)
                        register_quarantine(digest,row[0])
                    else:
                        print('El archivo origen no existe')


    except IOError as e:
            print('Error (0) in move the files')
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
            print(digest)
            #COMPROBAR

            for a in imagenes:
             query = '[Files].[getFiles]  ' + "'" + digest + "', " + str(id)+ ", '" +a+"'"

            con_sql = mssql_connection()
            data = get_data_from_sql(query)
            if len(data) <= 0:
                print('No data from database')
                for filename in imagenes:
                    register_files(digest, id, filename)
                sys.exit(0)
            else:
                for row in data:
                    if row[0] == digest:
                        print("Same files")

                        # si los datos son iguales, no pasa nada
                    elif row[0]!= digest:
                        # si hay un valor nuevo, que lo registe
                        print("There are more files, its  isnot int Database")




    except IOError as e:
            print('Error (0) in register Files, and also look at if ....').format(e.errno, e.strerror)
    finally:
            con_sql.close()

