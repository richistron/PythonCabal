#! /usr/bin/python3

'Importar tools.py'
print( 'Importar tools.py' )
import tools

'Inicializar mi robot'
print( 'Inicializar mi robot' )
r1 = tools.RobotPlus( 'Robocop' )

'Que me salude!'
print( 'Que me salude!' )
print(r1)

'Ir a todos los rincones'
print( 'Ir a todos los rincones' )
for direccion in [ 'N', 'NE', 'E', 'SE', 'S', 'SO', 'O', 'NO' ]:
    print( r1.avanza( direccion ) )

'Intentar algunos randoms'
print( 'Intentar algunos randoms' )
for i in range( 10 ):
    print( r1.avanza( None, None, 1 ) )
