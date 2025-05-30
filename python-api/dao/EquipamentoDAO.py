from dao.Database import Database
from model.Equipamento import Equipamento

class EquipamentoDAO:
    def __init__(self, db: Database | None = None):
        self.db = db or Database()

    def inserir(self, equipamento: Equipamento) -> int:
        sql = "INSERT INTO equipamento (tag, numero_patrimonio, id_modelo, id_laboratorio) VALUES (%(tag)s, %(numero_patrimonio)s, %(id_modelo)s, %(id_laboratorio)s)"
        params = {
            'tag': equipamento.tag,
            'numero_patrimonio': equipamento.numero_patrimonio,
            'id_modelo': equipamento.id_modelo,
            'id_laboratorio': equipamento.id_laboratorio
        }
        return self.db.insert(sql, params)

    def atualizar(self, equipamento: Equipamento) -> int:
        sql = " UPDATE equipamento SET tag = %(tag)s, numero_patrimonio = %(numero_patrimonio)s, id_modelo = %(id_modelo)s, id_laboratorio = %(id_laboratorio)s WHERE id = %(id)s"
        params = {
            'id': equipamento.id,
            'tag': equipamento.tag,
            'numero_patrimonio': equipamento.numero_patrimonio,
            'id_modelo': equipamento.id_modelo,
            'id_laboratorio': equipamento.id_laboratorio
        }
        return self.db.update(sql, params)

    def deletar(self, id: int) -> int:
        return self.db.delete("DELETE FROM equipamento WHERE id = %(id)s", {'id': id})

    def buscar_por_id(self, id: int) -> Equipamento | None:
        resultado = self.db.select("SELECT * FROM equipamento WHERE id = %(id)s", {'id': id})
        return Equipamento(**resultado[0]) if resultado else None
    
    def buscar_por_id_laboratorio(self, id: int, id_laboratorio: int) -> Equipamento | None:
        resultado = self.db.select("SELECT * FROM equipamento WHERE id = %(id)s AND id_laboratorio = %(id_laboratorio)s", {'id': id, 'id_laboratorio': id_laboratorio})
        return Equipamento(**resultado[0]) if resultado else None

    def listar_todos(self) -> list[Equipamento]:
        resultados = self.db.select("SELECT * FROM equipamento ORDER BY numero_patrimonio")
        return [Equipamento(**linha) for linha in resultados]
    
    def listar_por_laboratorio(self, id_laboratorio: int) -> list[Equipamento]:
        resultados = self.db.select("SELECT * FROM equipamento WHERE id_laboratorio = %(id_laboratorio)s ORDER BY numero_patrimonio", {'id_laboratorio': id_laboratorio})
        return [Equipamento(**linha) for linha in resultados]
