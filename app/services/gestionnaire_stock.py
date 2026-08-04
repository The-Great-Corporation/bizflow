import json
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
        
    def calculer_marge(self, produit: Produit) -> float:
        return produit.prix_vente - produit.prix_achat
    def produit_en_alerte(self) -> list[Produit]:
        return [produit for produit in self.produits if produit.quantite <= produit.seuil_alerte]
    
    def sauvegarder_donnees(self, chemin: str = "donnees/stock.json"):
        donnees = {
            "produits": [
                {
                    "nom": produit.nom,
                    "reference": produit.reference,
                    "prix_achat": produit.prix_achat,
                    "prix_vente": produit.prix_vente,
                    "quantite": produit.quantite,
                    "seuil_alerte": produit.seuil_alerte
                } for produit in self.produits
            ]
             }
        with open(chemin, "w", encoding="utf-8") as fichier:
            json.dump(donnees, fichier, ensure_ascii=False, indent=4)
            
    def charger_donnees(self, chemin: str = "donnees/stock.json"):
        with open(chemin, "r", encoding="utf-8") as fichier:
            donnees = json.load(fichier)
        self.produits = [Produit(**produit_dict) for produit_dict in donnees["produits" ]]