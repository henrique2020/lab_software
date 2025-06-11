from dao.Database import Database
from model.Certificado import Certificado

from dao.EventoDAO import EventoDAO

class CertificadoDAO:
    def __init__(self, db: Database | None = None):
        self.db = db or Database()
    
    def _buscar_objetos(self, linha: dict) -> Certificado:
        c = Certificado(**linha)
        c.id_evento = EventoDAO(self.db).buscar_por_id(c.id_evento)
        
        return c

    def inserir(self, certificado: Certificado) -> int:
        sql = "INSERT INTO certificado (id_evento, numero, data, orgao_expedidor, arquivo) VALUES (%(id_evento)s, %(numero)s, %(data)s, %(orgao_expedidor)s, %(arquivo)s)"
        params = {
            'id_evento': certificado.id_evento,
            'numero': certificado.numero,
            'data': certificado.data,
            'orgao_expedidor': certificado.orgao_expedidor,
            'arquivo': certificado.arquivo
        }
        return self.db.insert(sql, params)

    def atualizar(self, certificado: Certificado) -> int:
        sql = "UPDATE certificado SET numero = %(numero)s, data = %(data)s, orgao_expedidor = %(orgao_expedidor)s, arquivo = %(arquivo)s WHERE id_evento = %(id_evento)s"
        params = {
            'id_evento': certificado.id_evento,
            'numero': certificado.numero,
            'data': certificado.data,
            'orgao_expedidor': certificado.orgao_expedidor,
            'arquivo': certificado.arquivo
        }
        return self.db.update(sql, params)

    def deletar(self, id_evento: int) -> int:
        sql = "DELETE FROM certificado WHERE id_evento = %(id_evento)s"
        return self.db.delete(sql, {'id_evento': id_evento})

    def buscar_por_id(self, id_evento: int) -> Certificado | None:
        sql = "SELECT * FROM certificado WHERE id_evento = %(id_evento)s"
        resultado = self.db.select(sql, {'id_evento': id_evento})
        return Certificado(**resultado[0]) if resultado else None
    
    def listar_todos(self) -> list[Certificado]:
        sql = "SELECT * FROM certificado ORDER BY data"
        resultados = self.db.select(sql)
        return [self._buscar_objetos(linha) for linha in resultados]