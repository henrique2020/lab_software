from dataclasses import dataclass
from typing import Optional

@dataclass
class EquipamentoModelo:
    id: Optional[int]
    numero_patrimonio: int
    identificacao: str
    equipamento: str
    marca: str
    criterio_aceitacao_calibracao: str
    periodicidade_calibracao: int
    periodicidade_manutencao: int
    tipo: str  # '-', 'A', 'D'
    id_categoria: Optional[int]
