from dao.Database import Database
from model.Evento import Evento

class EventoDAO:
    def __init__(self, db: Database | None = None):
        self.db = db or Database()

    def inserir(self, evento: Evento) -> int:
        sql = "INSERT INTO evento (id_equipamento, tipo, data_agendada, descricao, status, custo)VALUES (%(id_equipamento)s, %(tipo)s, %(data_agendada)s, %(descricao)s, %(status)s, %(custo)s)"
        params = {
            'id_equipamento': evento.id_equipamento,
            'tipo': evento.tipo,
            'data_agendada': evento.data_agendada,
            'descricao': evento.descricao,
            'status': evento.status,
            'custo': evento.custo,
        }
        return self.db.insert(sql, params)

    def atualizar(self, evento: Evento) -> int:
        sql = " UPDATE evento SET id_equipamento = %(id_equipamento)s, tipo = %(tipo)s, data_agendada = %(data_agendada)s, descricao = %(descricao)s, status = %(status)s, custo = %(custo)s WHERE id = %(id)s"
        params = {
            'id': evento.id,
            'id_equipamento': evento.id_equipamento,
            'tipo': evento.tipo,
            'data_agendada': evento.data_agendada,
            'descricao': evento.descricao,
            'status': evento.status,
            'custo': evento.custo
        }
        return self.db.update(sql, params)

    def deletar(self, id: int) -> int:
        return self.db.delete("DELETE FROM evento WHERE id = %(id)s", {'id': id})

    def buscar_por_id(self, id: int) -> Evento | None:
        resultado = self.db.select("SELECT * FROM evento WHERE id = %(id)s", {'id': id})
        return Evento(**resultado[0]) if resultado else None
    
    def buscar_por_id_laboratorio(self, id: int, id_laboratorio: int) -> Evento | None:
        resultado = self.db.select("SELECT ev.* FROM evento ev JOIN equipamento eq ON (eq.id = ev.id_equipamento) WHERE ev.id = %(id)s AND eq.id_laboratorio = %(id_laboratorio)s", {'id': id, 'id_laboratorio': id_laboratorio})
        return Evento(**resultado[0]) if resultado else None

    def listar_todos(self) -> list[Evento]:
        resultados = self.db.select("SELECT * FROM evento ORDER BY data_agendada DESC")
        return [Evento(**linha) for linha in resultados]

    def listar_por_equipamento(self, id_equipamento: int) -> list[Evento]:
        resultados = self.db.select(
            "SELECT * FROM evento WHERE id_equipamento = %(id_equipamento)s ORDER BY data_agendada DESC",
            {'id_equipamento': id_equipamento}
        )
        return [Evento(**linha) for linha in resultados]
    
    def listar_por_equipamento_laboratorio(self, id_equipamento: int, id_laboratorio) -> list[Evento]:
        resultados = self.db.select(
            "SELECT ev.* FROM evento ev JOIN equipamento eq ON (eq.id = ev.id_equipamento) WHERE ev.id_equipamento = %(id_equipamento)s AND eq.id_laboratorio = %(id_laboratorio)s",
            {'id_equipamento': id_equipamento, 'id_laboratorio': id_laboratorio}
        )
        return [Evento(**linha) for linha in resultados]
    
    def listar_por_laboratorio(self, id_laboratorio: int) -> list[Evento]:
        resultados = self.db.select(
            "SELECT ev.* FROM evento ev JOIN equipamento eq ON (eq.id = ev.id_equipamento) WHERE eq.id_laboratorio = %(id_laboratorio)s",
            {'id_laboratorio': id_laboratorio}
        )
        return [Evento(**linha) for linha in resultados]
