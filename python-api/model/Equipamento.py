from dataclasses import dataclass
from typing import Optional
from datetime import date

from model.EquipamentoModelo import EquipamentoModelo
from model.Laboratorio import Laboratorio

@dataclass
class Equipamento:
    id: Optional[int]
    tag: int
    numero_patrimonio: int
    data_implantacao: date
    id_modelo: int|EquipamentoModelo
    id_laboratorio: int|Laboratorio
    ativo: Optional[bool] = True