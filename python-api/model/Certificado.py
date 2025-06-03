from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass
class Certificado:
    id: Optional[int]
    numero: int
    data: date
    orgao_expedidor: str
    arquivo: str