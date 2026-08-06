from dataclasses import dataclass


@dataclass
class Produit:
    nom: str
    reference: str
    prix_achat: float
    prix_vente: float
    quantite: int
    seuil_alerte: int
