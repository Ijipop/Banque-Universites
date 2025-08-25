#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de test et démonstration pour le système Universités/Facultés
Montre la relation 1-à-N et les listes dépendantes
"""

from database import (session, Universite, Faculte, 
                     obtenir_universites, obtenir_facultes_par_universite,
                     ajouter_faculte, initialiser_donnees)

def test_relation_1_to_n():
    """Test de la relation 1-à-N entre Universités et Facultés"""
    print("=== TEST RELATION 1-À-N ===")
    
    # Vérifier qu'une université peut avoir plusieurs facultés
    udem = session.query(Universite).filter_by(nom="Université de Montréal").first()
    if udem:
        print(f"Université : {udem.nom}")
        print(f"Nombre de facultés : {len(udem.facultes)}")
        print("Facultés :")
        for faculte in udem.facultes:
            print(f"  - {faculte.nom} ({faculte.code_faculte})")
    
    print()

def test_contrainte_cle_etrangere():
    """Test de la contrainte de clé étrangère"""
    print("=== TEST CONTRAINTE CLÉ ÉTRANGÈRE ===")
    
    try:
        # Essayer de créer une faculté sans université valide (doit échouer)
        faculte_invalide = Faculte(
            nom="Faculté Test",
            code_faculte="TEST",
            nombre_etudiants=100,
            universite_id=99999  # ID qui n'existe pas
        )
        session.add(faculte_invalide)
        session.commit()
        print("ERREUR : La faculté a été créée sans université valide!")
        
    except Exception as e:
        session.rollback()
        print(f"CORRECT : Impossible de créer une faculté sans université valide")
        print(f"Erreur : {e}")
    
    print()

def test_ajout_avec_validation():
    """Test de l'ajout avec validation"""
    print("=== TEST AJOUT AVEC VALIDATION ===")
    
    # Test 1 : Ajouter une faculté à une université existante (doit réussir)
    print("Test 1 : Ajout valide")
    result = ajouter_faculte("Faculté de Test", "TEST", 500, 1)
    if result:
        print("Faculté ajoutée avec succès")
    else:
        print("Échec de l'ajout")
    
    # Test 2 : Ajouter une faculté à une université inexistante (doit échouer)
    print("\nTest 2 : Université inexistante")
    result = ajouter_faculte("Faculté Test", "TEST2", 100, 99999)
    if result:
        print("La faculté a été ajoutée malgré l'université inexistante!")
    else:
        print("Ajout correctement refusé")
    
    # Test 3 : Ajouter une faculté en double (doit échouer)
    print("\nTest 3 : Faculté en double")
    result = ajouter_faculte("Faculté des Arts et Sciences", "FAS2", 1000, 1)
    if result:
        print("Faculté en double ajoutée!")
    else:
        print("Doublon correctement refusé")
    
    print()

def test_cascade_delete():
    """Test de la suppression en cascade"""
    print("=== TEST SUPPRESSION EN CASCADE ===")
    
    # Créer une université de test avec des facultés
    univ_test = Universite(nom="Université Test", code_universite="TEST", ville="Ville Test")
    session.add(univ_test)
    session.flush()
    
    # Ajouter des facultés à l'université test
    faculte1 = Faculte(nom="Faculté Test 1", code_faculte="T1", nombre_etudiants=100, universite_id=univ_test.id)
    faculte2 = Faculte(nom="Faculté Test 2", code_faculte="T2", nombre_etudiants=200, universite_id=univ_test.id)
    
    session.add_all([faculte1, faculte2])
    session.commit()
    
    print(f"Université créée : {univ_test.nom} avec {len(univ_test.facultes)} facultés")
    
    # Compter avant suppression
    nb_facultes_avant = session.query(Faculte).filter_by(universite_id=univ_test.id).count()
    print(f"Facultés avant suppression : {nb_facultes_avant}")
    
    # Supprimer l'université (doit supprimer les facultés automatiquement)
    session.delete(univ_test)
    session.commit()
    
    # Compter après suppression
    nb_facultes_apres = session.query(Faculte).filter_by(universite_id=univ_test.id).count()
    print(f"Facultés après suppression : {nb_facultes_apres}")
    
    if nb_facultes_apres == 0:
        print("Suppression en cascade fonctionnelle")
    else:
        print("Problème avec la suppression en cascade")
    
    print()

def afficher_donnees_completes():
    """Affiche toutes les données de la base"""
    print("=== DONNÉES COMPLÈTES DE LA BASE ===")
    
    universites_liste = obtenir_universites()
    
    for universite in universites_liste:
        print(f"\n{universite.nom} ({universite.code_universite}) - {universite.ville}")
        facultes = obtenir_facultes_par_universite(universite.id)
        
        if facultes:
            for faculte in facultes:
                print(f"  - {faculte.nom} ({faculte.code_faculte}) : {faculte.nombre_etudiants} étudiants")
        else:
            print("  (Aucune faculté)")
    
    print(f"\nTOTAL : {len(universites_liste)} universités, {session.query(Faculte).count()} facultés")
    print()

def demonstration_listes_dependantes():
    """Simule le comportement des listes dépendantes"""
    print("=== SIMULATION LISTES DÉPENDANTES ===")
    
    print("1. Liste des universités disponibles :")
    universites_liste = obtenir_universites()
    for i, universite in enumerate(universites_liste, 1):
        print(f"   {i}. {universite.nom}")
    
    print("\n2. Sélection de l'Université de Montréal :")
    udem = session.query(Universite).filter_by(nom="Université de Montréal").first()
    if udem:
        print(f"   Université sélectionnée : {udem.nom}")
        
        print("\n3. Facultés disponibles pour l'Université de Montréal :")
        facultes_udem = obtenir_facultes_par_universite(udem.id)
        for i, faculte in enumerate(facultes_udem, 1):
            print(f"   {i}. {faculte.nom} ({faculte.code_faculte})")
    
    print("\n4. Sélection de l'Université Laval :")
    ulaval = session.query(Universite).filter_by(nom="Université Laval").first()
    if ulaval:
        print(f"   Université sélectionnée : {ulaval.nom}")
        
        print("\n5. Facultés disponibles pour l'Université Laval :")
        facultes_ulaval = obtenir_facultes_par_universite(ulaval.id)
        for i, faculte in enumerate(facultes_ulaval, 1):
            print(f"   {i}. {faculte.nom} ({faculte.code_faculte})")
    
    print()

if __name__ == "__main__":
    print(" DÉMONSTRATION COMPLÈTE - SYSTÈME UNIVERSITÉS/FACULTÉS")
    print("=" * 60)
    
    # Initialiser les données
    initialiser_donnees()
    
    try:
        # Exécuter tous les tests
        test_relation_1_to_n()
        test_contrainte_cle_etrangere()
        test_ajout_avec_validation()
        test_cascade_delete()
        afficher_donnees_completes()
        demonstration_listes_dependantes()
        
        print("TOUS LES TESTS TERMINÉS AVEC SUCCÈS!")
        
    except Exception as e:
        session.rollback()
        print(f"Erreur lors des tests : {e}")
    finally:
        session.close()
