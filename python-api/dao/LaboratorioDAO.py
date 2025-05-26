from dao.Database import Database
from model.Laboratorio import Laboratorio

class LaboratorioDAO:
    def __init__(self, db: Database | None = None):
        self.db = db or Database()

    def inserir(self, laboratorio: Laboratorio) -> int:
        sql = """
        INSERT INTO laboratorio (nome, sigla, bloco, sala)
        VALUES (%(nome)s, %(sigla)s, %(bloco)s, %(sala)s)
        """
        params = {
            'nome': laboratorio.nome,
            'sigla': laboratorio.sigla,
            'bloco': laboratorio.bloco,
            'sala': laboratorio.sala
        }
        return self.db.insert(sql, params)

    def atualizar(self, laboratorio: Laboratorio) -> int:
        sql = """
        UPDATE laboratorio SET
            nome = %(nome)s,
            sigla = %(sigla)s,
            bloco = %(bloco)s,
            sala = %(sala)s
        WHERE id = %(id)s
        """
        params = {
            'id': laboratorio.id,
            'nome': laboratorio.nome,
            'sigla': laboratorio.sigla,
            'bloco': laboratorio.bloco,
            'sala': laboratorio.sala
        }
        return self.db.update(sql, params)

    def deletar(self, id_: int) -> int:
        sql = "DELETE FROM laboratorio WHERE id = %(id)s"
        return self.db.delete(sql, {'id': id_})

    def listar_todos(self) -> list[Laboratorio]:
        sql = "SELECT * FROM laboratorio ORDER BY nome"
        resultados = self.db.select(sql)
        return [Laboratorio(**linha) for linha in resultados]

    def buscar_por_id(self, id_: int) -> Laboratorio | None:
        sql = "SELECT * FROM laboratorio WHERE id = %(id)s"
        resultado = self.db.select(sql, {'id': id_})
        return Laboratorio(**resultado[0]) if resultado else None
