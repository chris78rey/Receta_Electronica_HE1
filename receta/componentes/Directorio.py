import os


class ListaManagerReceta(object):
    def __init__(self, directorio):
        self.directorio = directorio

    def setlistas(self, lista01, lista02):
        self.lista01 = lista01
        self.lista02 = lista02

    def comparaListasc(self):
        setlista01 = set(self.lista01)
        setlista02 = set(self.lista02)

        resultado = setlista01.difference(setlista02)
        return list(resultado)

    def listapdf(self):
        ejemplo_dir = self.directorio
        contenido = os.listdir(ejemplo_dir)
        recetas = []
        for fichero in contenido:
            if os.path.isfile(os.path.join(ejemplo_dir, fichero)):
                if fichero.endswith("pdf"):
                    recetas.append(fichero)
        return recetas
