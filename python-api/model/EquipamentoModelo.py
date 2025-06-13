from dataclasses import dataclass
from typing import Optional

from model.Categoria import Categoria

@dataclass
class EquipamentoModelo:
    id: Optional[int]
    numero_patrimonio: int
    identificacao: str
    equipamento: str
    marca: str
    criterio_aceitacao_calibracao: str
    periodicidade_calibracao: int   #Anos
    aviso_renovacao_calibracao: int #Dias
    periodicidade_manutencao: int   #Anos
    tipo: str  #A', 'D'
    id_categoria: Optional[int]|Optional[Categoria]
    ativo: Optional[bool] = True
