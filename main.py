import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Qt
from interface import Ui_MainWindow
from database import (session, Universite, Faculte,
                        obtenir_universites, obtenir_facultes_par_universite,
                        ajouter_faculte, initialiser_donnees)

class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialiser la base de données
        initialiser_donnees()

        # Connecter les signaux aux méthodes
        self.connecter_signaux()

        # Charger les données initiales
        self.charger_universites()

        # Message de bienvenue
        self.ui.textEdit_resultats.append("Application démarrée. Sélectionnez une université pour voir ses facultés.")

    def connecter_signaux(self):
        # Signal principal : changement de universités met à jour les facultés
        self.ui.comboBox_universites.currentTextChanged.connect(self.on_universites_change)
        
        # Changement de facultés active le bouton d'affichage
        self.ui.comboBox_facultes.currentTextChanged.connect(self.on_facultes_change)
        
        # Boutons d'action
        self.ui.pushButton_AfficherSelection.clicked.connect(self.afficher_selection)
        self.ui.pushButton_AjouterUniversite.clicked.connect(self.ajouter_nouvelle_universite)
        self.ui.pushButton_AjouterFaculte.clicked.connect(self.ajouter_nouvelle_faculte)
        self.ui.pushButton_VoirStats.clicked.connect(self.voir_statistiques)
        self.ui.pushButton_Demo.clicked.connect(self.lancer_demonstration)
        self.ui.pushButton_ViderMessages.clicked.connect(self.vider_messages)

    def charger_universites(self):
        try:
            # Vider les ComboBox
            self.ui.comboBox_universites.clear()
            self.ui.comboBox_facultes.clear()
            self.ui.comboBox_universite_faculte.clear()  # Ajout de cette ligne
            
            # Ajouter l'option par défaut
            defaut_item: str = "-- Choisir une université --"
            self.ui.comboBox_universites.addItem(defaut_item, None)
            self.ui.comboBox_universite_faculte.addItem(defaut_item, None)
            
            # Récupérer et ajouter tous les universite
            universite_liste = obtenir_universites()
            
            for universite in universite_liste:
                # Stocker l'ID du universite comme data
                self.ui.comboBox_universites.addItem(universite.nom, universite.id)
                self.ui.comboBox_universite_faculte.addItem(universite.nom, universite.id)
            
            self.ui.textEdit_resultats.append(f"Liste des universités chargées : {len(universite_liste)} universités disponibles")
            
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Erreur lors du chargement des universités : {e}")
    
    def on_universites_change(self):
        # Récupérer l'ID de l'iniversité sélectionnée
        universite_id = self.ui.comboBox_universites.currentData()
        universite_nom = self.ui.comboBox_universites.currentText()
        
        # Vider la liste des facultés
        self.ui.comboBox_facultes.clear()
        
        if universite_id is None:
            # Aucun université sélectionné
            self.ui.comboBox_facultes.setEnabled(False)
            self.ui.pushButton_AfficherSelection.setEnabled(False)
            self.ui.comboBox_facultes.addItem("-- Sélectionnez d'abord l'université --")
            return
        
        try:
            # Récupérer les facultés du université sélectionné
            facultes = obtenir_facultes_par_universite(universite_id)
            
            if facultes:
                # Activer la ComboBox des facultés
                self.ui.comboBox_facultes.setEnabled(True)
                self.ui.comboBox_facultes.addItem("-- Choisir une faculté --", None)
                
                # Ajouter toutes les facultés
                for faculte in facultes:
                    self.ui.comboBox_facultes.addItem(
                        f"{faculte.nom} ({faculte.code_faculte})",
                        faculte.id
                    )
                
                self.ui.textEdit_resultats.append(
                    f"Université sélectionnée : {universite_nom} - {len(facultes)} faculté(s) disponible(s)"
                )
                
            else:
                # Aucune faculté pour ce université
                self.ui.comboBox_facultes.setEnabled(False)
                self.ui.comboBox_facultes.addItem("Aucune facultés disponible")
                self.ui.textEdit_resultats.append(f"Université sélectionnée : {universite_nom} - Aucune faculté")
                
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Erreur lors du chargement des facultés : {e}")
    
    def on_facultes_change(self):
        faculte_id = self.ui.comboBox_facultes.currentData()
        
        # Activer/désactiver le bouton d'affichage selon la sélection
        if faculte_id is not None:
            self.ui.pushButton_AfficherSelection.setEnabled(True)
        else:
            self.ui.pushButton_AfficherSelection.setEnabled(False)
    
    def afficher_selection(self):
        universite_nom = self.ui.comboBox_universites.currentText()
        faculte_nom = self.ui.comboBox_facultes.currentText()
        
        if self.ui.comboBox_universites.currentData() and self.ui.comboBox_facultes.currentData():
            message = f"SÉLECTION ACTUELLE :\n"
            message += f"  Université : {universite_nom}\n"
            message += f"  Faculté : {faculte_nom}"
            
            QMessageBox.information(self, "Sélection Actuelle", message)
            self.ui.textEdit_resultats.append(f"Affichage : {universite_nom} > {faculte_nom}")
        else:
            QMessageBox.critical(self, "Erreur", f"Rien de selectionner")
    
    def ajouter_nouvelle_universite(self):
        try:
            nom_uni = self.ui.lineEdit_nom_universite.text().strip().title()
            ville_uni = self.ui.lineEdit_ville_universite.text().strip().title()
            code_uni = self.ui.lineEdit_code_universite.text().strip().upper()
            annee = int(self.ui.lineEdit_annee_universite.text().strip())
            
            # Validations
            if not nom_uni:
                QMessageBox.warning(self, "Validation", "Le nom de l'université est obligatoire!")
                return

            if not ville_uni:
                QMessageBox.warning(self, "Validation", "La ville de l'université est obligatoire!")
                return
            
            if not code_uni or len(code_uni) > 10:
                QMessageBox.warning(self, "Validation", "Le code doit faire maximum 10 caractères!")
                return
            
            if annee and annee < 1000:
                QMessageBox.warning(self, "Validation", "L'année de fondation doit être supérieure à 1000!")
                return
            
            # Vérifier que l'université n'existe pas déjà
            universite_existant = session.query(Universite).filter(
                (Universite.nom == nom_uni) | (Universite.code_universite == code_uni) | (Universite.ville == ville_uni) | (Universite.annee_fondation == annee)
            ).first()
            
            if universite_existant:
                QMessageBox.warning(self, "Erreur", f"Cette université existe déjà!")
                return
            
            # Créer la nouvelle université
            nouvelle_universite = Universite(nom=nom_uni, ville=ville_uni, code_universite=code_uni, annee_fondation=annee)
            session.add(nouvelle_universite)
            session.commit()
            
            # Succès
            self.ui.textEdit_resultats.append(f"NOUVELLE UNIVERSITÉ AJOUTÉE : {nom_uni} ({code_uni})")
            
            # Vider les champs
            self.ui.lineEdit_nom_universite.clear()
            self.ui.lineEdit_ville_universite.clear()
            self.ui.lineEdit_code_universite.clear()
            self.ui.lineEdit_annee_universite.clear()
            
            # Recharger les listes
            self.charger_universites()
            
            QMessageBox.information(self, "Succès", f"Université '{nom_uni}' ajoutée avec succès!")
            
        except Exception as e:
            session.rollback()
            QMessageBox.critical(self, "Erreur", f"Erreur lors de l'ajout de l'université : {e}")
    
    def ajouter_nouvelle_faculte(self):
        try:
            # Récupérer les données du formulaire
            nom_faculte = self.ui.lineEdit_nom_faculte.text().strip().title()
            code_faculte = self.ui.lineEdit_code_faculte.text().strip().upper()
            nb_etudiants = int(self.ui.lineEditl_nbEtudiants_faculte.text().strip())
            id_uni = self.ui.comboBox_universite_faculte.currentData()
            nom_uni = self.ui.comboBox_universite_faculte.currentText()
            
            # Validations
            if not nom_faculte:
                QMessageBox.warning(self, "Validation", "Le nom de la faculté est obligatoire!")
                return
            
            if id_uni is None:
                QMessageBox.warning(self, "Validation", "Veuillez sélectionner l'université parent!")
                return

            if not code_faculte:
                QMessageBox.warning(self, "Validation", "Le code de la faculté est obligatoire!")
                return
            
            if not nb_etudiants:
                nb_etudiants = 0
            
            # Ajouter la faculté via la fonction de la base de données
            nouvelle_faculte = ajouter_faculte(nom_faculte, code_faculte, nb_etudiants, id_uni)
            
            if nouvelle_faculte:
                # Succès
                self.ui.textEdit_resultats.append(f"AJOUT RÉUSSI : {nom_faculte} ({code_faculte}) ajoutée à {nom_uni}")
                
                # Vider les champs
                self.ui.lineEdit_nom_faculte.clear()
                self.ui.lineEdit_code_faculte.clear()
                self.ui.lineEditl_nbEtudiants_faculte.clear()
                self.ui.comboBox_universite_faculte.setCurrentIndex(0)
                
                # Actualiser les listes si l'université actuel correspond
                if self.ui.comboBox_universites.currentData() == id_uni:
                    self.on_universites_change()
                
                QMessageBox.information(
                    self, 
                    "Succès", 
                    f"Faculté '{nom_faculte}' ajoutée avec succès à {nom_uni}!"
                )
            else:
                # Échec (message déjà affiché par la fonction)
                QMessageBox.warning(self, "Erreur", "Impossible d'ajouter la faculté. Vérifiez les logs.")
                
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Erreur lors de l'ajout : {e}")
    
    def voir_statistiques(self):
        try:
            nb_uni = session.query(Universite).count()
            nb_facul = session.query(Faculte).count()
            
            # Détail par pays
            message = f"STATISTIQUES DE LA BASE DE DONNÉES\n\n"
            message += f"Total : {nb_uni} université, {nb_facul} facultés\n\n"
            
            liste_uni = obtenir_universites()
            for uni in liste_uni:
                nb_facul_uni = len(uni.facultes)
                message += f"• {uni.nom} ({uni.code_universite}) : {nb_facul_uni} faculté(s)\n"
            
            QMessageBox.information(self, "Statistiques", message)
            
            self.ui.textEdit_resultats.append(f"Statistiques : {nb_uni} université, {nb_facul} facultés")
            
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Erreur lors du calcul des statistiques : {e}")

    def lancer_demonstration(self):
        chosen_uni = "UQAM"
        chosen_facul = "Faculté des Arts (ARTS)"
        
        self.ui.textEdit_resultats.append("\n=== DÉMONSTRATION COMPLÈTE ===")
        
        # 1. Afficher les statistiques
        self.voir_statistiques()
        
        # 2. Sélectionner automatiquement une université
        index_uni = self.ui.comboBox_universites.findText(chosen_uni)
        if index_uni >= 0:
            self.ui.comboBox_universites.setCurrentIndex(index_uni)
            self.ui.textEdit_resultats.append(f"1. Sélection automatique de l'université '{chosen_uni}'")
            
            # 3. Sélectionner une faculté
            index_falcu = self.ui.comboBox_facultes.findText(chosen_facul, Qt.MatchContains)
            if index_falcu >= 0:
                self.ui.comboBox_facultes.setCurrentIndex(index_falcu)
                self.ui.textEdit_resultats.append(f"2. Sélection automatique de la faculté '{chosen_facul}'")
                
                # 4. Afficher la sélection
                self.afficher_selection()
        
        self.ui.textEdit_resultats.append("=== DÉMONSTRATION TERMINÉE ===\n")

    def vider_messages(self):
        self.ui.textEdit_resultats.clear()
        # self.ui.textEdit_resultats.append("Messages vidés.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = Application()
    window.show()
    
    sys.exit(app.exec())