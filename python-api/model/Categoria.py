from dataclasses import dataclass
from typing import Optional

@dataclass
class Categoria:
    id: Optional[int]
    nome: str