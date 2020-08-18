from receta.componentes.Directorio import ListaManagerReceta
from receta.componentes.BaseDatos import RecetaHe1, session
from receta.componentes.mensaje import Email_HE1, clavecorreosender
from sqlalchemy.orm.query import Query
import time


class Infraestructura(object):
    def __init__(self, path_archivos, sender):
        self.file_base = path_archivos
        self.sender = sender


    def ejecuta_flujo(self):
        file_base = self.file_base

        lm = ListaManagerReceta(file_base)

        lista = session.query(RecetaHe1).all()

        listadebase = []

        for itera in lista:
            listadebase.append(itera.archivo)

        lista_archivos_pdf_so = lm.listapdf()

        lm.setlistas(lista_archivos_pdf_so, listadebase)
        # me da solo los archivos que faltan
        # los que ya estando en base no_se_comparan
        lista_resultado = lm.comparaListasc()

        for archivo in lista_resultado:
            receta = RecetaHe1(archivo)
            session.add(receta)
        session.commit()

        archivo_attachment = file_base

        subject = '''
        FACTURACION HE1
        '''
        sender = self.sender
        receiver = ''
        body = '''
        Estimado Paciente
        Este es un mail autogenerado por el SISTEMA DE FACTURACION ELECTRÓNICA del HE-1.
        NOTA: no lo responda
        '''
        smtp = 'smtp.gmail.com'
        port = 587

        lista = session.query(RecetaHe1).filter(RecetaHe1.enviado == 0)

        for indice in lista:
            try:
                time.sleep(0.25)
                archivo_attachment = file_base + indice.archivo
                receiver = indice.email
                ehe1 = Email_HE1(subject, sender, receiver, body,
                                 archivo_attachment, smtp, port, clavecorreosender)
                ehe1.enviar_mensaje()
                indice.enviado = 1
                objetoregistro = session.query(RecetaHe1).filter(RecetaHe1.id == indice.id).first()
                objetoregistro.enviado = 1
                session.merge(objetoregistro)
                session.commit()
            except AssertionError as error:
                print(error)
