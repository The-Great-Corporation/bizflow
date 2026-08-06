from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from app.models.produit import Produit


class TypeMouvement(Enum):
    ENTREE = "ENTREE"
    SORTIE = "SORTIE"


@dataclass
class MouvementStock:
    produit: Produit
    type_mouvement: TypeMouvement
    quantite: int
    date: datetime
