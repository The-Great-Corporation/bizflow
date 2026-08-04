from app.models.produit import Produit

class GestionnaireStock:
    def __init__(self):
        self.produits = []
        
    def ajouter_produit(self, produit: Produit):
        self.produits.append(produit)