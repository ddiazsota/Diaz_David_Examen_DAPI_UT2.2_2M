def leerDocumento(LibroCuentas):
    """Esta función leera la información de un fichero y la guardara
      en una variable de tipo lista.Donde cada uno de los datos de la
      lista será una línea de documento
      Parámetros:
        -Ruta de acceso al fichero a leer
    Salida
        -Lista con los datos de un fichero"""
    
    file=open('LibroCuentas.txt','r')
    lineas=file.readlines()
    return lineas

def IdentificarPagado():
    """Esta función crea un fichero llamado 'Pagado.txt'
        donde escribirán todas las líneas donde en la 
        lista aparezca la palabra 'Pagado'
        Parámetros:
            -No tiene
        Salida:
            -No tiene"""
    lineas=[]
    file=open('Pagado.txt', 'a')
    
    file.write('Pagado', '\n')
    
        
        
    


        