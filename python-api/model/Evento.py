from dataclasses import dataclass
from typing import Optional
from datetime import datetime, date

from model.Equipamento import Equipamento

@dataclass
class Evento:
    id: Optional[int]
    id_equipamento : int|Equipamento
    tipo: str  # 'Calibracao','Manutencao','Qualificacao','Checagem'
    data_criacao: datetime
    data_agendada: date
    descricao: str
    custo: Optional[float] = None