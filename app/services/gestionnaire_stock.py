from app.models.produit import Produit
from app.models.mouvement_stock import MouvementStock, TypeMouvement

class GestionnaireStock:
    def __init__(self):
        self.produits = []
        self.mouvements = []
    def ajouter_produit(self, produit: Produit):
        self.produits.append(produit)
        
    def enregistrer_mouvement(self, mouvement:MouvementStock):
        if mouvement.type_mouvement == TypeMouvement.SORTIE:
            if mouvement.quantite > mouvement.produit.quantite:
                raise ValueError(f"Quantité insuffisante pour le produit {mouvement.produit.nom}: {mouvement.produit.quantite} disponible, {mouvement.quantite} demandé.")
            mouvement.produit.quantite -= mouvement.quantite
        else:
            mouvement.produit.quantite += mouvement.quantite
        self.mouvements.append(mouvement)