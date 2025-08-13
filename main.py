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
            
            # Ajouter l'option par défaut
            defaut_item: str = "-- Choisir une universit\u00e9 --"
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
                self.ui.comboBox_facultes.addItem("-- Choisir une facult\u00e9 --", None)
                
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
        print("changement de facultés active le bouton d'affichage")

        faculte_id = self.ui.comboBox_facultes.currentData()
        
        # Activer/désactiver le bouton d'affichage selon la sélection
        if faculte_id is not None:
            self.ui.pushButton_AfficherSelection.setEnabled(True)
        else:
            self.ui.pushButton_AfficherSelection.setEnabled(False)
    
    def afficher_selection(self):
        print("Afficher selection")
        """Affiche les détails de la sélection actuelle"""
        
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
        print("Ajouter université")
    
    def ajouter_nouvelle_faculte(self):
        print("Ajouter facultés")
    
    def voir_statistiques(self):
        print("Afficher statistiques")

    def lancer_demonstration(self):
        print("Demo")

    def vider_messages(self):
        self.ui.textEdit_resultats.clear()
        # self.ui.textEdit_resultats.append("Messages vidés.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = Application()
    window.show()
    
    sys.exit(app.exec())