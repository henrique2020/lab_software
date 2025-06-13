from dao.Database import Database
from model.Laboratorio import Laboratorio

from dao.BlocoDAO import BlocoDAO

class LaboratorioDAO:
    def __init__(self, db: Database | None = None):
        self.db = db or Database()
        
    def _buscar_objetos(self, linha: dict) -> Laboratorio:
        l = Laboratorio(**linha)
        l.id_bloco = BlocoDAO(self.db).buscar_por_id(l.id_bloco)
        
        return l

    def inserir(self, laboratorio: Laboratorio) -> int:
        sql = "INSERT INTO laboratorio (nome, sigla, id_bloco, sala) VALUES (%(nome)s, %(sigla)s, %(id_bloco)s, %(sala)s)"
        params = {
            'nome': laboratorio.nome,
            'sigla': laboratorio.sigla,
            'id_bloco': laboratorio.id_bloco,
            'sala': laboratorio.sala
        }
        return self.db.insert(sql, params)

    def atualizar(self, laboratorio: Laboratorio) -> int:
        sql = "UPDATE laboratorio SET nome = %(nome)s, sigla = %(sigla)s, id_bloco = %(id_bloco)s, sala = %(sala)s WHERE id = %(id)s"
        params = {
            'id': laboratorio.id,
            'nome': laboratorio.nome,
            'sigla': laboratorio.sigla,
            'id_bloco': laboratorio.id_bloco,
            'sala': laboratorio.sala
        }
        return self.db.update(sql, params)

    def deletar(self, id_: int) -> int:
        sql = "DELETE FROM laboratorio WHERE id = %(id)s"
        return self.db.delete(sql, {'id': id_})

    def buscar_por_id(self, id_: int) -> Laboratorio | None:
        sql = "SELECT * FROM laboratorio WHERE id = %(id)s"
        resultado = self.db.select(sql, {'id': id_})
        return Laboratorio(**resultado[0]) if resultado else None
    
    def listar_todos(self) -> list[Laboratorio]:
        sql = "SELECT * FROM laboratorio ORDER BY nome"
        resultados = self.db.select(sql)
        return [self._buscar_objetos(linha) for linha in resultados]

    def atualizar_status(self, id: int) -> bool:
        sql = "UPDATE laboratorio SET ativo = CASE WHEN ativo = 1 THEN 0 ELSE 1 END WHERE id = %(id)s"
        return self.db.update(sql, {'id': id})
