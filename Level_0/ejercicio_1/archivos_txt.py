class Txt():
    """
    Clase para interactuar con archivos de text.
    """

    def __init__(self, archivo):
        self.archivo = f'{archivo}.txt'

    def crear_txt(self,):
        self.archivo_creado = open(self.archivo, 'w')
        return self.archivo_creado

    def leer_txt(self,):
        with open(self.archivo, 'r') as self.archivo_leido:
            mensaje = self.archivo_leido.read()
        return mensaje

    def escribir_txt(self, texto):
        with open(self.archivo, 'a') as self.texto_agregado:
            self.texto_agregado.write(f'{texto}')
        return self.texto_agregado


if __name__ == '__main__':
    prueba = Txt('probando')
    prueba.escribir_txt('probando\n')
    prueba.escribir_txt('tini tini tini\n')
    print(prueba.leer_txt())
