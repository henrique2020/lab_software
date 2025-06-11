from dataclasses import dataclass
from typing import Optional
from datetime import date

from model.Evento import Evento

@dataclass
class Certificado:
    id: Optional[int]
    id_evento: int|Evento
    numero: int
    data: date
    orgao_expedidor: str
    arquivo: str