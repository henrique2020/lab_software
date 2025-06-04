from dataclasses import dataclass
from typing import Optional
from datetime import datetime, date

@dataclass
class Evento:
    id: Optional[int]
    id_equipamento : int
    tipo: str  # 'Calibracao','Manutencao','Qualificacao','Checagem'
    data_criacao: datetime
    data_agendada: date
    descricao: str
    status : str = 'Pendente'   # 'Aprovado', 'Pendente', 'Recusado'
    custo: Optional[float] = None