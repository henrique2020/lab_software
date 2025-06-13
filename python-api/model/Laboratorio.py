from dataclasses import dataclass
from typing import Optional

from model.Bloco import Bloco

@dataclass
class Laboratorio:
    id: Optional[int]
    nome: str
    sigla: str
    id_bloco: int|Bloco
    sala: int
    ativo: Optional[bool] = True
