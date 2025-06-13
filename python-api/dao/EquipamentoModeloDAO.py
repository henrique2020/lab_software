from dao.Database import Database
from model.EquipamentoModelo import EquipamentoModelo

from dao.CategoriaDAO import CategoriaDAO

class EquipamentoModeloDAO:
    def __init__(self, db: Database | None = None):
        self.db = db or Database()
    
    def _buscar_objetos(self, linha: dict) -> EquipamentoModelo:
        e = EquipamentoModelo(**linha)
        e.id_categoria = CategoriaDAO(self.db).buscar_por_id(e.id_categoria)
        
        return e

    def inserir(self, modelo: EquipamentoModelo) -> int:
        sql = "INSERT INTO equipamento_modelo (numero_patrimonio, identificacao, equipamento, marca, criterio_aceitacao_calibracao, periodicidade_calibracao, periodicidade_manutencao, tipo, id_categoria) VALUES (%(numero_patrimonio)s, %(identificacao)s, %(equipamento)s, %(marca)s, %(criterio)s, %(periodicidade_calibracao)s, %(periodicidade_manutencao)s, %(tipo)s, %(id_categoria)s)"
        params = {
            'numero_patrimonio': modelo.numero_patrimonio,
            'identificacao': modelo.identificacao,
            'equipamento': modelo.equipamento,
            'marca': modelo.marca,
            'criterio': modelo.criterio_aceitacao_calibracao,
            'periodicidade_calibracao': modelo.periodicidade_calibracao,
            'periodicidade_manutencao': modelo.periodicidade_manutencao,
            'tipo': modelo.tipo,
            'id_categoria': modelo.id_categoria,
        }
        return self.db.insert(sql, params)

    def atualizar(self, modelo: EquipamentoModelo) -> int:
        sql = " UPDATE equipamento_modelo SET numero_patrimonio = %(numero_patrimonio)s, identificacao = %(identificacao)s, equipamento = %(equipamento)s, marca = %(marca)s, criterio_aceitacao_calibracao = %(criterio_aceitacao_calibracao)s, periodicidade_calibracao = %(periodicidade_calibracao)s, periodicidade_manutencao = %(periodicidade_manutencao)s, tipo = %(tipo)s, id_categoria = %(id_categoria)s WHERE id = %(id)s"
        params = {
            'id': modelo.id,
            'numero_patrimonio': modelo.numero_patrimonio,
            'identificacao': modelo.identificacao,
            'equipamento': modelo.equipamento,
            'marca': modelo.marca,
            'criterio_aceitacao_calibracao': modelo.criterio_aceitacao_calibracao,
            'periodicidade_calibracao': modelo.periodicidade_calibracao,
            'periodicidade_manutencao': modelo.periodicidade_manutencao,
            'tipo': modelo.tipo,
            'id_categoria': modelo.id_categoria,
        }
        return self.db.update(sql, params)

    def deletar(self, id: int) -> int:
        return self.db.delete("DELETE FROM equipamento_modelo WHERE id = %(id)s", {'id': id})

    def buscar_por_id(self, id: int) -> EquipamentoModelo | None:
        resultado = self.db.select("SELECT * FROM equipamento_modelo WHERE id = %(id)s", {'id': id})
        return EquipamentoModelo(**resultado[0]) if resultado else None

    def listar_todos(self) -> list[EquipamentoModelo]:
        resultados = self.db.select("SELECT * FROM equipamento_modelo ORDER BY numero_patrimonio")
        return [self._buscar_objetos(linha) for linha in resultados]

    def atualizar_status(self, id: int) -> bool:
        sql = "UPDATE equipamento_modelo SET ativo = CASE WHEN ativo = 1 THEN 0 ELSE 1 END WHERE id = %(id)s"
        return self.db.update(sql, {'id': id})