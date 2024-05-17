
"""1. Cree un sistema de banca en línea con las siguientes características:

* Los usuarios deben poder iniciar sesión con un nombre de usuario y contraseña.
* Si el usuario ingresa las credenciales incorrectas tres veces, el sistema debe bloquearlas.
*El saldo inicial en la cuenta bancaria es de $2000.
* El sistema debe permitir a los usuarios depositar, retirar, ver y transferir dinero.
* El sistema debe mostrar un menú para que los usuarios realicen transacciones.
"""


class Menu_principal():
    """
    Muestra las opciones del menu principal.
    """

    def __init__(self) -> None:
        self.menu_inicio()

    def menu_inicio(self,):
        print('Bienvenido al BBVA', '\n',
              '\n' 'Elija una opcion para continuar:')
        seleccion = int(input())
        print(f'La opcion {seleccion} ha sido sellecionada')
        return seleccion


class Registro():
    """
    Crea un usuario nuevo y lo guarda.
    """

    def __init__(self) -> None:
        self.nuevo_usuario()
        self.saldo = 2000

    def nuevo_usuario(self,):
        pass


class Login(Registro):
    """
    Sirve para entrar al sistema, si ya existe un registro previo.
    """

    def __init__(self) -> None:
        self.ingreso()

    def ingreso(self,):
        pass

    def bloqueo_clave(self,):
        pass


class Menu():
    """
    Muestra en pantalla las diferentes operaciones disponibles.
    """

    def __init__(self) -> None:
        self.menu(self,)

    def menu(self,):
        pass


class Visualizar():
    """
    Muestra el saldo de la cuenta.
    """

    def __init__(self) -> None:
        self.mostrar_saldo(self,)

    def mostrar_saldo(self,):
        pass


class Depositar():
    """
    Sirve para ingresar dinero en la cuenta.
    """

    def __init__(self) -> None:
        self.ingresar_dinero(self,)

    def ingresar_dinero(self,):
        pass


class Retirar():
    """
    Sirve para retirar dinero en la cuenta.
    """

    def __init__(self) -> None:
        self.retirar_dinero(self,)

    def retirar_dinero(self,):
        pass


class Transferir():
    """
    Sirve para transferir dinero hacia otra cuenta.
    """

    def __init__(self) -> None:
        self.transferir_dinero(self,)

    def transferir_dinero(self,):
        pass


# class App():
    """
    Ejecuta la app.
    """
    # Menu_principal()


if __name__ == '__main__':
    # App()

   ### probando lectura de datos ###
    path = 'C:\\Users\\CHIKY\\OneDrive\\Escritorio\\repositorios\\Ejercicios\\Level_0\\ejercicio_1\\clientes.txt'
    fichero = open(path, 'a')
    user = 'max'
    passw = '2234'

    fichero.write(f'{user}.{passw}\n')
    fichero.close()

    lectura = open(path, 'r')

    for x in lectura:
        if x == 'leo.123\n':
            print('usuario logueado')
            break
        else:
            print(x)
