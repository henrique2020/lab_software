from dataclasses import dataclass
from typing import Optional

@dataclass
class Equipamento:
    id: Optional[int]
    tag: int
    numero_patrimonio: int
    id_modelo: int
    id_laboratorio: int