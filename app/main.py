from datetime import datetime

from app.models.mouvement_stock import MouvementStock, TypeMouvement
from app.models.produit import Produit
from app.services.gestionnaire_stock import GestionnaireStock


def afficher_menu():
    print("\n===== BizFlow - Gestion de stock =====")
    print("1. Ajouter un produit")
    print("2. Lister les produits")
    print("3. Enregistrer un mouvement de stock")
    print("4. Voir les produits en alerte")
    print("5. Sauvegarder et quitter")


def ajouter_produit(gestion: GestionnaireStock):
    nom = input("Nom du produit : ")
    reference = input("Référence : ")
    prix_achat = float(input("Prix d'achat : "))
    prix_vente = float(input("Prix de vente : "))
    quantite = int(input("Quantité initiale : "))
    seuil_alerte = int(input("Seuil d'alerte : "))

    produit = Produit(
        nom=nom,
        reference=reference,
        prix_achat=prix_achat,
        prix_vente=prix_vente,
        quantite=quantite,
        seuil_alerte=seuil_alerte,
    )
    gestion.ajouter_produit(produit)
    print(f"Produit '{nom}' ajouté avec succès.")


def lister_produits(gestion: GestionnaireStock):
    if not gestion.produits:
        print("Aucun produit en stock.")
        return
    for produit in gestion.produits:
        print(f"- {produit.nom} ({produit.reference}) : {produit.quantite} unités")


def enregistrer_mouvement(gestion: GestionnaireStock):
    reference = input("Référence du produit : ")
    produit_trouve = None
    for produit in gestion.produits:
        if produit.reference == reference:
            produit_trouve = produit
            break

    if produit_trouve is None:
        print("Produit introuvable.")
        return

    type_saisi = input("Type de mouvement (entree/sortie) : ").strip().lower()
    quantite = int(input("Quantité : "))

    type_mouvement = (
        TypeMouvement.ENTREE if type_saisi == "entree" else TypeMouvement.SORTIE
    )

    mouvement = MouvementStock(
        produit=produit_trouve,
        type_mouvement=type_mouvement,
        quantite=quantite,
        date=datetime.now(),
    )

    try:
        gestion.enregistrer_mouvement(mouvement)
        print("Mouvement enregistré avec succès.")
    except ValueError as erreur:
        print(f"Erreur : {erreur}")


def produit_en_alerte(gestion: GestionnaireStock):
    alertes = gestion.produit_en_alerte()
    if not alertes:
        print("Aucun produit en alerte.")
        return
    for produit in alertes:
        print(
            f"⚠️ {produit.nom} : {produit.quantite} restants (seuil : {produit.seuil_alerte})"
        )


def main():
    gestion = GestionnaireStock()

    try:
        gestion.charger_donnees()
        print("Données chargées avec succès.")
    except FileNotFoundError:
        print("Aucune sauvegarde trouvée, démarrage avec un stock vide.")

    while True:
        afficher_menu()
        choix = input("Votre choix : ")

        if choix == "1":
            ajouter_produit(gestion)
        elif choix == "2":
            lister_produits(gestion)
        elif choix == "3":
            enregistrer_mouvement(gestion)
        elif choix == "4":
            produit_en_alerte(gestion)
        elif choix == "5":
            gestion.sauvegarder_donnees()
            print("Données sauvegardées. À bientôt !")
            break
        else:
            print("Choix invalide, réessayez.")


if __name__ == "__main__":
    main()
