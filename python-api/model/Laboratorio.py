from dataclasses import dataclass
from typing import Optional

@dataclass
class Laboratorio:
    id: Optional[int]
    nome: str
    sigla: str
    bloco: str
    sala: int
