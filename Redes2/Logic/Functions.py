from Redes2.data.ConfigurationDB import  get_data_from_sql
from Redes2.data.ConfigurationDB import  mssql_connection
import sys
def registerCustomers (card,password):
    try:
        query = '[Customer].[registerCustomer] ' + "'"+card+"'" + "," + "'"+password+"'"
        con_sql = mssql_connection()
        data = get_data_from_sql(query)

        if len(data) <= 0:
            print('No data')
            sys.exit(0)
        else:
            print('Se ha registrado correctamente')
        #return 0
    except IOError as e:
        print('Error (0) in register Student').format(e.errno, e.strerror)
    finally:
        con_sql.close()


def autentication_customers(card):
    try:
        query = '[Customer].[autentication] ' + "'"+card+"'"
        con_sql = mssql_connection()
        data = get_data_from_sql(query)

        if len(data) <= 0:
            print('No data')
            sys.exit(0)
        else:
            for row in (data):
                print(row)
                if range(len(row) > 0):
                    print('Correcto'+data(row))
                else:
                    print('iNCORRECTO'+(range(row)))
    except IOError as e:
        print('Error (0) in register Student').format(e.errno, e.strerror)
    finally:
        con_sql.close()
