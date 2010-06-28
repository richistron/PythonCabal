'''Herramientas para PythonCabal

Rutinas para todo el grupo
'''

class Robot:
    "Un robot con nombre, posición y dirección."

    def __init__( self, nombre, posicion = (0,0), direccion = 'N', distancia = 1 ):
        "Constructor"
        self.nombre = nombre
        self.x, self.y = posicion
        self.direccion = direccion
        self.distancia = distancia

    def avanza( self, direccion = '', distancia = 1, random = None, rango = (0, 10) ):
        "Avanza posición del robot y regresa nueva posición. Opcionalmente, cambia su dirección."
        if random:
            import random
            
            r1, r2 = rango
            self.x = random.randint(r1, r2)
            self.y = random.randint(r1, r2)
            
            
            rd = random.sample( [ 'N', 'NE', 'E', 'SE', 'S', 'SO', 'O', 'NO' ], 1)
            self.direccion = rd[0]
            
            self.distancia = random.randint(r1, r2)
        else:
            if direccion:
                self.direccion = direccion
            if distancia:
                self.distancia = distancia

        if self.direccion == 'N':
            self.y = self.y + self.distancia
        elif self.direccion == 'NE':
            self.x = self.x + self.distancia
            self.y = self.y + self.distancia
        elif self.direccion == 'E':
            self.x = self.x + self.distancia
        elif self.direccion == 'SE':
            self.x = self.x + self.distancia
            self.y = self.y - self.distancia
        elif self.direccion == 'S':
            self.y = self.y - self.distancia
        elif self.direccion == 'SO':
            self.x = self.x - self.distancia
            self.y = self.y - self.distancia
        elif self.direccion == 'O':
            self.x = self.x - self.distancia
        elif self.direccion == 'NO':
            self.x = self.x - self.distancia
            self.y = self.y + self.distancia
        return self.x, self.y

class RobotPlus( Robot ):
    "Robot que reporta."

    def reporta( self ):
        return 'Soy ' + self.nombre + ' y estoy en (' + str(self.x) + ', ' +str(self.y) + '), ' + self.direccion

    def __repr__( self ):
        return self.reporta()

def ponComa( numero ):
    '''Regresa numero como cadena con comas.

    numero es un entero
    no maneja signo'''
    particion = str( numero ).partition('.')
    cadena = particion[0]
    while indice > 3:
        '''Restar 3 al indice'''
        indice = indice - 3
        
        '''Agregar coma'''
        cadena = cadena[ :indice ] +  ',' + cadena[ indice: ]
        
    
    '''Regresar resultado con todo y parte decimal'''
    return cadena + particion[1] + particion[2]

if __name__ == '__main__':
    for datoDePrueba in [ 0, 12, 123, 1234, 12345, 123456, 1234567, 1234.5678 ]:
        print ( datoDePrueba , ponComa( datoDePrueba ) )
