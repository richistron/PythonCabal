'''Herramientas para PythonCabal

Rutinas para todo el grupo
'''

def ponComa( numero ):
    '''Regresa numero como cadena con comas.

    numero es un entero
    no maneja signo ni punto decimal.'''
    entero = int( numero )
    fraccion = numero - entero
    cadena = str( numero )

    if fraccion != 0.0:
        indice = len( str( entero ) )
    else:
        indice = len( cadena )

    while indice > 3:
        indice = indice - 3
        cadena = cadena[ :indice ] +  ',' + cadena[ indice: ]
    
    return cadena

if __name__ == '__main__':
    for datoDePrueba in [ 0, 12, 123, 1234, 12345, 123456, 1234567, 19234.3498 ]:
        print ( datoDePrueba , ponComa( datoDePrueba ) )
