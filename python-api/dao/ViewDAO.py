from dao.Database import Database

class ViewDAO:
    def __init__(self, db: Database | None = None):
        self.db = db or Database()
        
    def listar_disponibilidade(self) -> dict:
        return self.db.select("""
            SELECT l.sigla Sigla, em.equipamento Equipamento, eq.tag TAG, c.data Certificado, 
                CASE
                    WHEN CURDATE() < DATE_ADD(c.data, INTERVAL em.periodicidade_calibracao YEAR) THEN 'Disponível'
                    ELSE 'Indisponível'
                END 'Status',
                CASE
                    WHEN c.id IS NOT NULL THEN DATE_ADD(c.data, INTERVAL em.periodicidade_calibracao YEAR)
                    WHEN ev.id IS NOT NULL THEN DATE_ADD(ev.data_agendada, INTERVAL 1 DAY)
                    ELSE CURDATE()
                END ProximaCalibracaoNecessaria
            FROM equipamento eq
            LEFT JOIN (
                SELECT *, ROW_NUMBER() OVER(PARTITION BY id_equipamento ORDER BY id DESC) AS pos 
                FROM evento
                WHERE data_agendada < CURDATE()
            ) ev ON ev.id_equipamento = eq.id AND ev.pos = 1
            LEFT JOIN certificado c ON c.id_evento = ev.id
            JOIN laboratorio l ON l.id = eq.id_laboratorio
            JOIN equipamento_modelo em ON em.id = eq.id_modelo
        """)
        
    def avisos_certifiado(self, id_laboratorio: int|None =  None) -> dict:
        params = None
        where = ''
        if(id_laboratorio):
            params = {'id_laboratorio': id_laboratorio}
            where = 'AND l.id = %(id_laboratorio)s'
        
        
        return self.db.select(f"""
            SELECT l.sigla Sigla, em.equipamento Equipamento, eq.tag TAG, 
                CASE
                    WHEN CURDATE() < DATE_ADD(c.data, INTERVAL em.periodicidade_calibracao YEAR) THEN 'Disponível'
                    WHEN ev.data_agendada IS NOT NULL AND ev.tipo = 'CALIBRACAO' THEN 'Agendado'
                    ELSE 'Indisponível'
                END 'Status',
                DATEDIFF(
                    CASE
                        WHEN c.id IS NOT NULL THEN DATE_ADD(c.data, INTERVAL em.periodicidade_calibracao YEAR)
                        WHEN ev.id IS NOT NULL THEN ev.data_agendada
                        ELSE CURDATE()
                    END, CURDATE()) CertificadoExpiraEm
            FROM equipamento eq
            LEFT JOIN (
                SELECT *, ROW_NUMBER() OVER(PARTITION BY id_equipamento ORDER BY id DESC) AS pos 
                FROM evento
            ) ev ON ev.id_equipamento = eq.id AND ev.pos = 1
            LEFT JOIN certificado c ON c.id_evento = ev.id
            JOIN laboratorio l ON l.id = eq.id_laboratorio
            JOIN equipamento_modelo em ON em.id = eq.id_modelo
            WHERE DATEDIFF(
                    CASE
                        WHEN c.id IS NOT NULL THEN DATE_ADD(c.data, INTERVAL em.periodicidade_calibracao YEAR)
                        WHEN ev.id IS NOT NULL THEN DATE_ADD(ev.data_agendada, INTERVAL 1 DAY)
                        ELSE CURDATE()
                    END, CURDATE()) <= em.aviso_renovacao_calibracao {where}
        """, params)