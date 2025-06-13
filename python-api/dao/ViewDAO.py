from dao.Database import Database

class ViewDAO:
    def __init__(self, db: Database | None = None):
        self.db = db or Database()
        
    def listar_disponibilidade(self):
        return self.db.select("""
            SELECT l.sigla Sigla, em.equipamento Equipamento, eq.tag TAG, c.data Certificado, 
                CASE
                    WHEN DATE(NOW()) < DATE_ADD(c.data, INTERVAL em.periodicidade_calibracao YEAR) THEN 'Disponível'
                    ELSE 'Indisponível'
                END 'Status',
                CASE
                    WHEN c.id IS NOT NULL THEN DATE_ADD(c.data, INTERVAL em.periodicidade_calibracao YEAR)
                    WHEN ev.id IS NOT NULL THEN DATE_ADD(ev.data_agendada, INTERVAL 1 DAY)
                    ELSE DATE(NOW())
                END ProximaCalibracaoNecessaria
            FROM equipamento eq
            LEFT JOIN (
                SELECT *, ROW_NUMBER() OVER(PARTITION BY id_equipamento ORDER BY id DESC) AS pos 
                FROM evento
                WHERE data_agendada < DATE(NOW())
            ) ev ON ev.id_equipamento = eq.id AND ev.pos = 1
            LEFT JOIN certificado c ON c.id_evento = ev.id
            JOIN laboratorio l ON l.id = eq.id_laboratorio
            JOIN equipamento_modelo em ON em.id = eq.id_modelo
        """)