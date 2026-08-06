from datetime import datetime

import pytest

from app.models.mouvement_stock import MouvementStock, TypeMouvement
from app.models.produit import Produit
from app.services.gestionnaire_stock import GestionnaireStock


def test_ajouter_produit():
    gestion = GestionnaireStock()
    savon = Produit(
        nom="Savon noir",
        reference="SAV001",
        prix_achat=2.0,
        prix_vente=5.0,
        quantite=20,
        seuil_alerte=5,
    )

    gestion.ajouter_produit(savon)

    assert savon in gestion.produits
    assert len(gestion.produits) == 1


def test_enregistrer_mouvement_entree():
    gestion = GestionnaireStock()
    savon = Produit(
        nom="Savon noir",
        reference="SAV001",
        prix_achat=2.0,
        prix_vente=5.0,
        quantite=20,
        seuil_alerte=5,
    )
    gestion.ajouter_produit(savon)

    entree = MouvementStock(
        produit=savon,
        type_mouvement=TypeMouvement.ENTREE,
        quantite=10,
        date=datetime.now(),
    )
    gestion.enregistrer_mouvement(entree)

    assert savon.quantite == 30


def test_enregistrer_mouvement_sortie_insuffisante():
    gestion = GestionnaireStock()
    savon = Produit(
        nom="Savon noir",
        reference="SAV001",
        prix_achat=2.0,
        prix_vente=5.0,
        quantite=5,
        seuil_alerte=5,
    )
    gestion.ajouter_produit(savon)

    sortie = MouvementStock(
        produit=savon,
        type_mouvement=TypeMouvement.SORTIE,
        quantite=100,
        date=datetime.now(),
    )

    with pytest.raises(ValueError):
        gestion.enregistrer_mouvement(sortie)


def test_calculer_marge():
    gestion = GestionnaireStock()
    savon = Produit(
        nom="Savon noir",
        reference="SAV001",
        prix_achat=2.0,
        prix_vente=5.0,
        quantite=20,
        seuil_alerte=5,
    )

    marge = gestion.calculer_marge(savon)

    assert marge == 3.0


def test_produit_en_alerte():
    gestion = GestionnaireStock()
    savon = Produit(
        nom="Savon noir",
        reference="SAV001",
        prix_achat=2.0,
        prix_vente=5.0,
        quantite=3,
        seuil_alerte=5,
    )
    shampoing = Produit(
        nom="Shampoing",
        reference="SHA001",
        prix_achat=3.0,
        prix_vente=7.0,
        quantite=20,
        seuil_alerte=5,
    )

    gestion.ajouter_produit(savon)
    gestion.ajouter_produit(shampoing)

    alertes = gestion.produit_en_alerte()

    assert savon in alertes
    assert shampoing not in alertes
