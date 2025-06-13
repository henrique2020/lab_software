from dataclasses import dataclass
from typing import Optional

@dataclass
class Bloco:
    id: Optional[int]
    nome: str
    ativo: Optional[bool] = True