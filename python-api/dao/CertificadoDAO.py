from dao.Database import Database
from model.Certificado import Certificado

class CertificadoDAO:
    def __init__(self, db: Database | None = None):
        self.db = db or Database()

    def inserir(self, certificado: Certificado) -> int:
        sql = "INSERT INTO certificado (numero, data, orgao_expedidor, arquivo) VALUES (%(numero)s, %(data)s, %(orgao_expedidor)s, %(arquivo)s)"
        params = {
            'numero': certificado.numero,
            'data': certificado.data,
            'orgao_expedidor': certificado.orgao_expedidor,
            'arquivo': certificado.arquivo
        }
        return self.db.insert(sql, params)

    def atualizar(self, certificado: Certificado) -> int:
        sql = "UPDATE certificado SET numero = %(numero)s, data = %(data)s, orgao_expedidor = %(orgao_expedidor)s, arquivo = %(arquivo)s WHERE id = %(id)s"
        params = {
            'id': certificado.id,
            'numero': certificado.numero,
            'data': certificado.data,
            'orgao_expedidor': certificado.orgao_expedidor,
            'arquivo': certificado.arquivo
        }
        return self.db.update(sql, params)

    def deletar(self, id_: int) -> int:
        sql = "DELETE FROM certificado WHERE id = %(id)s"
        return self.db.delete(sql, {'id': id_})

    def buscar_por_id(self, id_: int) -> Certificado | None:
        sql = "SELECT * FROM certificado WHERE id = %(id)s"
        resultado = self.db.select(sql, {'id': id_})
        return Certificado(**resultado[0]) if resultado else None
    
    def listar_todos(self) -> list[Certificado]:
        sql = "SELECT * FROM certificado ORDER BY data"
        resultados = self.db.select(sql)
        return [Certificado(**linha) for linha in resultados]