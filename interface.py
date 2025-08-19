# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 840)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupe_selection = QGroupBox(self.centralwidget)
        self.groupe_selection.setObjectName(u"groupe_selection")
        self.groupe_selection.setGeometry(QRect(10, 10, 881, 141))
        font = QFont()
        font.setBold(True)
        self.groupe_selection.setFont(font)
        self.layoutWidget = QWidget(self.groupe_selection)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 861, 111))
        self.layout_selection = QVBoxLayout(self.layoutWidget)
        self.layout_selection.setSpacing(6)
        self.layout_selection.setObjectName(u"layout_selection")
        self.layout_selection.setContentsMargins(0, 0, 0, 0)
        self.layout_combos = QHBoxLayout()
        self.layout_combos.setSpacing(6)
        self.layout_combos.setObjectName(u"layout_combos")
        self.layout_universites = QVBoxLayout()
        self.layout_universites.setObjectName(u"layout_universites")
        self.labelUniversites = QLabel(self.layoutWidget)
        self.labelUniversites.setObjectName(u"labelUniversites")
        self.labelUniversites.setMaximumSize(QSize(16777215, 25))
        font1 = QFont()
        font1.setBold(False)
        self.labelUniversites.setFont(font1)

        self.layout_universites.addWidget(self.labelUniversites)

        self.comboBox_universites = QComboBox(self.layoutWidget)
        self.comboBox_universites.setObjectName(u"comboBox_universites")
        self.comboBox_universites.setMinimumSize(QSize(0, 30))
        self.comboBox_universites.setFont(font1)

        self.layout_universites.addWidget(self.comboBox_universites)


        self.layout_combos.addLayout(self.layout_universites)

        self.layout_facultes = QVBoxLayout()
        self.layout_facultes.setObjectName(u"layout_facultes")
        self.label_facultes = QLabel(self.layoutWidget)
        self.label_facultes.setObjectName(u"label_facultes")
        self.label_facultes.setMaximumSize(QSize(16777215, 25))
        self.label_facultes.setFont(font1)

        self.layout_facultes.addWidget(self.label_facultes)

        self.comboBox_facultes = QComboBox(self.layoutWidget)
        self.comboBox_facultes.setObjectName(u"comboBox_facultes")
        self.comboBox_facultes.setEnabled(False)
        self.comboBox_facultes.setMinimumSize(QSize(0, 30))
        self.comboBox_facultes.setFont(font1)

        self.layout_facultes.addWidget(self.comboBox_facultes)


        self.layout_combos.addLayout(self.layout_facultes)


        self.layout_selection.addLayout(self.layout_combos)

        self.pushButton_AfficherSelection = QPushButton(self.layoutWidget)
        self.pushButton_AfficherSelection.setObjectName(u"pushButton_AfficherSelection")
        self.pushButton_AfficherSelection.setMinimumSize(QSize(0, 45))
        self.pushButton_AfficherSelection.setFont(font1)

        self.layout_selection.addWidget(self.pushButton_AfficherSelection)

        self.groupe_resultats = QGroupBox(self.centralwidget)
        self.groupe_resultats.setObjectName(u"groupe_resultats")
        self.groupe_resultats.setGeometry(QRect(10, 490, 881, 321))
        self.groupe_resultats.setFont(font)
        self.layoutWidget1 = QWidget(self.groupe_resultats)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 20, 861, 291))
        self.layout_resultats = QVBoxLayout(self.layoutWidget1)
        self.layout_resultats.setObjectName(u"layout_resultats")
        self.layout_resultats.setContentsMargins(0, 0, 0, 0)
        self.layout_buttons = QHBoxLayout()
        self.layout_buttons.setObjectName(u"layout_buttons")

        self.pushButton_VoirStats = QPushButton(self.layoutWidget1)
        self.pushButton_VoirStats.setObjectName(u"pushButton_VoirStats")
        self.pushButton_VoirStats.setFont(font1)

        self.layout_buttons.addWidget(self.pushButton_VoirStats)

        self.pushButton_Demo = QPushButton(self.layoutWidget1)
        self.pushButton_Demo.setObjectName(u"pushButton_Demo")
        self.pushButton_Demo.setFont(font1)

        self.layout_buttons.addWidget(self.pushButton_Demo)

        self.pushButton_Supprimer = QPushButton(self.layoutWidget1)
        self.pushButton_Supprimer.setObjectName(u"pushButton_Supprimer")
        self.pushButton_Supprimer.setMaximumSize(QSize(75, 50))
        self.pushButton_Supprimer.setFont(font1)

        self.layout_buttons.addWidget(self.pushButton_Supprimer)


        self.layout_resultats.addLayout(self.layout_buttons)

        self.textEdit_resultats = QTextEdit(self.layoutWidget1)
        self.textEdit_resultats.setObjectName(u"textEdit_resultats")
        self.textEdit_resultats.setFont(font1)

        self.layout_resultats.addWidget(self.textEdit_resultats)

        self.pushButton_ViderMessages = QPushButton(self.layoutWidget1)
        self.pushButton_ViderMessages.setObjectName(u"pushButton_ViderMessages")
        self.pushButton_ViderMessages.setFont(font1)

        self.layout_resultats.addWidget(self.pushButton_ViderMessages)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 160, 881, 321))
        self.layout_ajout = QHBoxLayout(self.layoutWidget2)
        self.layout_ajout.setObjectName(u"layout_ajout")
        self.layout_ajout.setContentsMargins(0, 0, 0, 0)
        self.groupe_ajout_universite = QGroupBox(self.layoutWidget2)
        self.groupe_ajout_universite.setObjectName(u"groupe_ajout_universite")
        self.groupe_ajout_universite.setFont(font)
        self.layoutWidget3 = QWidget(self.groupe_ajout_universite)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 20, 421, 287))
        self.layout_ajout_universite = QVBoxLayout(self.layoutWidget3)
        self.layout_ajout_universite.setObjectName(u"layout_ajout_universite")
        self.layout_ajout_universite.setContentsMargins(0, 0, 0, 0)
        self.layout_nom_universite = QVBoxLayout()
        self.layout_nom_universite.setObjectName(u"layout_nom_universite")
        self.label_nom_universite = QLabel(self.layoutWidget3)
        self.label_nom_universite.setObjectName(u"label_nom_universite")
        self.label_nom_universite.setMaximumSize(QSize(16777215, 25))
        self.label_nom_universite.setFont(font1)

        self.layout_nom_universite.addWidget(self.label_nom_universite)

        self.lineEdit_nom_universite = QLineEdit(self.layoutWidget3)
        self.lineEdit_nom_universite.setObjectName(u"lineEdit_nom_universite")
        self.lineEdit_nom_universite.setMinimumSize(QSize(0, 30))
        self.lineEdit_nom_universite.setFont(font1)

        self.layout_nom_universite.addWidget(self.lineEdit_nom_universite)


        self.layout_ajout_universite.addLayout(self.layout_nom_universite)

        self.layout_ville_universite = QVBoxLayout()
        self.layout_ville_universite.setObjectName(u"layout_ville_universite")
        self.label_ville_universite = QLabel(self.layoutWidget3)
        self.label_ville_universite.setObjectName(u"label_ville_universite")
        self.label_ville_universite.setMaximumSize(QSize(16777215, 25))
        self.label_ville_universite.setFont(font1)

        self.layout_ville_universite.addWidget(self.label_ville_universite)

        self.lineEdit_ville_universite = QLineEdit(self.layoutWidget3)
        self.lineEdit_ville_universite.setObjectName(u"lineEdit_ville_universite")
        self.lineEdit_ville_universite.setMinimumSize(QSize(0, 30))
        self.lineEdit_ville_universite.setFont(font1)

        self.layout_ville_universite.addWidget(self.lineEdit_ville_universite)


        self.layout_ajout_universite.addLayout(self.layout_ville_universite)

        self.layout_code_universite = QVBoxLayout()
        self.layout_code_universite.setObjectName(u"layout_code_universite")
        self.label_code_universite = QLabel(self.layoutWidget3)
        self.label_code_universite.setObjectName(u"label_code_universite")
        self.label_code_universite.setMaximumSize(QSize(16777215, 25))
        self.label_code_universite.setFont(font1)

        self.layout_code_universite.addWidget(self.label_code_universite)

        self.lineEdit_code_universite = QLineEdit(self.layoutWidget3)
        self.lineEdit_code_universite.setObjectName(u"lineEdit_code_universite")
        self.lineEdit_code_universite.setMinimumSize(QSize(0, 30))
        self.lineEdit_code_universite.setFont(font1)

        self.layout_code_universite.addWidget(self.lineEdit_code_universite)


        self.layout_ajout_universite.addLayout(self.layout_code_universite)

        self.layout_annee_universite = QVBoxLayout()
        self.layout_annee_universite.setObjectName(u"layout_annee_universite")
        self.label_annee_universite = QLabel(self.layoutWidget3)
        self.label_annee_universite.setObjectName(u"label_annee_universite")
        self.label_annee_universite.setMaximumSize(QSize(16777215, 25))
        self.label_annee_universite.setFont(font1)

        self.layout_annee_universite.addWidget(self.label_annee_universite)

        self.lineEdit_annee_universite = QLineEdit(self.layoutWidget3)
        self.lineEdit_annee_universite.setObjectName(u"lineEdit_annee_universite")
        self.lineEdit_annee_universite.setMinimumSize(QSize(0, 30))
        self.lineEdit_annee_universite.setFont(font1)

        self.layout_annee_universite.addWidget(self.lineEdit_annee_universite)


        self.layout_ajout_universite.addLayout(self.layout_annee_universite)

        self.pushButton_AjouterUniversite = QPushButton(self.layoutWidget3)
        self.pushButton_AjouterUniversite.setObjectName(u"pushButton_AjouterUniversite")
        # self.pushButton_AjouterUniversite.setEnabled(False)
        self.pushButton_AjouterUniversite.setMinimumSize(QSize(0, 45))
        self.pushButton_AjouterUniversite.setFont(font1)

        self.layout_ajout_universite.addWidget(self.pushButton_AjouterUniversite)


        self.layout_ajout.addWidget(self.groupe_ajout_universite)

        self.groupe_ajout_faculte = QGroupBox(self.layoutWidget2)
        self.groupe_ajout_faculte.setObjectName(u"groupe_ajout_faculte")
        self.groupe_ajout_faculte.setFont(font)
        self.layoutWidget4 = QWidget(self.groupe_ajout_faculte)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 20, 421, 287))
        self.layout_ajout_faculte = QVBoxLayout(self.layoutWidget4)
        self.layout_ajout_faculte.setObjectName(u"layout_ajout_faculte")
        self.layout_ajout_faculte.setContentsMargins(0, 0, 0, 0)
        self.layout_nom_faculte = QVBoxLayout()
        self.layout_nom_faculte.setObjectName(u"layout_nom_faculte")
        self.label_nom_faculte = QLabel(self.layoutWidget4)
        self.label_nom_faculte.setObjectName(u"label_nom_faculte")
        self.label_nom_faculte.setMaximumSize(QSize(16777215, 25))
        self.label_nom_faculte.setFont(font1)

        self.layout_nom_faculte.addWidget(self.label_nom_faculte)

        self.lineEdit_nom_faculte = QLineEdit(self.layoutWidget4)
        self.lineEdit_nom_faculte.setObjectName(u"lineEdit_nom_faculte")
        self.lineEdit_nom_faculte.setMinimumSize(QSize(0, 30))
        self.lineEdit_nom_faculte.setFont(font1)

        self.layout_nom_faculte.addWidget(self.lineEdit_nom_faculte)


        self.layout_ajout_faculte.addLayout(self.layout_nom_faculte)

        self.layout_universite_faculte = QVBoxLayout()
        self.layout_universite_faculte.setObjectName(u"layout_universite_faculte")
        self.label_universite_faculte = QLabel(self.layoutWidget4)
        self.label_universite_faculte.setObjectName(u"label_universite_faculte")
        self.label_universite_faculte.setMaximumSize(QSize(16777215, 25))
        self.label_universite_faculte.setFont(font1)

        self.layout_universite_faculte.addWidget(self.label_universite_faculte)

        self.comboBox_universite_faculte = QComboBox(self.layoutWidget4)
        self.comboBox_universite_faculte.setObjectName(u"comboBox_universite_faculte")
        self.comboBox_universite_faculte.setMinimumSize(QSize(0, 30))
        self.comboBox_universite_faculte.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_universite_faculte.setFont(font1)

        self.layout_universite_faculte.addWidget(self.comboBox_universite_faculte)


        self.layout_ajout_faculte.addLayout(self.layout_universite_faculte)

        self.layout_code_faculte = QVBoxLayout()
        self.layout_code_faculte.setObjectName(u"layout_code_faculte")
        self.label_code_faculte = QLabel(self.layoutWidget4)
        self.label_code_faculte.setObjectName(u"label_code_faculte")
        self.label_code_faculte.setMaximumSize(QSize(16777215, 25))
        self.label_code_faculte.setFont(font1)

        self.layout_code_faculte.addWidget(self.label_code_faculte)

        self.lineEdit_code_faculte = QLineEdit(self.layoutWidget4)
        self.lineEdit_code_faculte.setObjectName(u"lineEdit_code_faculte")
        self.lineEdit_code_faculte.setMinimumSize(QSize(0, 30))
        self.lineEdit_code_faculte.setFont(font1)

        self.layout_code_faculte.addWidget(self.lineEdit_code_faculte)


        self.layout_ajout_faculte.addLayout(self.layout_code_faculte)

        self.layout_nbEtudiants_faculte = QVBoxLayout()
        self.layout_nbEtudiants_faculte.setObjectName(u"layout_nbEtudiants_faculte")
        self.label_nbEtudiants_faculte = QLabel(self.layoutWidget4)
        self.label_nbEtudiants_faculte.setObjectName(u"label_nbEtudiants_faculte")
        self.label_nbEtudiants_faculte.setMaximumSize(QSize(16777215, 25))
        self.label_nbEtudiants_faculte.setFont(font1)

        self.layout_nbEtudiants_faculte.addWidget(self.label_nbEtudiants_faculte)

        self.lineEditl_nbEtudiants_faculte = QLineEdit(self.layoutWidget4)
        self.lineEditl_nbEtudiants_faculte.setObjectName(u"lineEditl_nbEtudiants_faculte")
        self.lineEditl_nbEtudiants_faculte.setMinimumSize(QSize(0, 30))
        self.lineEditl_nbEtudiants_faculte.setFont(font1)

        self.layout_nbEtudiants_faculte.addWidget(self.lineEditl_nbEtudiants_faculte)


        self.layout_ajout_faculte.addLayout(self.layout_nbEtudiants_faculte)

        self.pushButton_AjouterFaculte = QPushButton(self.layoutWidget4)
        self.pushButton_AjouterFaculte.setObjectName(u"pushButton_AjouterFaculte")
        # self.pushButton_AjouterFaculte.setEnabled(False)
        self.pushButton_AjouterFaculte.setMinimumSize(QSize(0, 45))
        self.pushButton_AjouterFaculte.setFont(font1)

        self.layout_ajout_faculte.addWidget(self.pushButton_AjouterFaculte)


        self.layout_ajout.addWidget(self.groupe_ajout_faculte)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Syst\u00e8me Universitaire", None))
        self.groupe_selection.setTitle(QCoreApplication.translate("MainWindow", u"S\u00e9lection avec Listes D\u00e9pendantes", None))
        self.labelUniversites.setText(QCoreApplication.translate("MainWindow", u"S\u00e9lectionnez une universit\u00e9  :", None))
        self.comboBox_universites.setPlaceholderText(QCoreApplication.translate("MainWindow", u"-- Choisir une universit\u00e9 --", None))
        self.label_facultes.setText(QCoreApplication.translate("MainWindow", u"S\u00e9lectionnez une facult\u00e9  :", None))
        self.comboBox_facultes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"-- Choisir une facult\u00e9 --", None))
        self.pushButton_AfficherSelection.setText(QCoreApplication.translate("MainWindow", u"Afficher S\u00e9lection", None))
        self.groupe_resultats.setTitle(QCoreApplication.translate("MainWindow", u"Informations et Messages", None))
        self.pushButton_VoirStats.setText(QCoreApplication.translate("MainWindow", u"Voir Statistiques", None))
        self.pushButton_Demo.setText(QCoreApplication.translate("MainWindow", u"D\u00e9monstration", None))
        self.pushButton_Supprimer.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.pushButton_ViderMessages.setText(QCoreApplication.translate("MainWindow", u"Vider les Messages", None))
        self.groupe_ajout_universite.setTitle(QCoreApplication.translate("MainWindow", u"Ajout une Universit\u00e9", None))
        self.label_nom_universite.setText(QCoreApplication.translate("MainWindow", u"Nom de l'universit\u00e9:", None))
        self.lineEdit_nom_universite.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom complet de l'universit\u00e9", None))
        self.label_ville_universite.setText(QCoreApplication.translate("MainWindow", u"Ville de l'universit\u00e9:", None))
        self.lineEdit_ville_universite.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ville o\u00f9 se trouve l'universit\u00e9", None))
        self.label_code_universite.setText(QCoreApplication.translate("MainWindow", u"Code de l'universit\u00e9:", None))
        self.lineEdit_code_universite.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Code unique pour l'universit\u00e9 (maximum 10 caractères)", None))
        self.label_annee_universite.setText(QCoreApplication.translate("MainWindow", u"Ann\u00e9e de fondation:", None))
        self.lineEdit_annee_universite.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ann\u00e9e de fondation (optionnel)", None))
        self.pushButton_AjouterUniversite.setText(QCoreApplication.translate("MainWindow", u"Ajouter Universit\u00e9", None))
        self.groupe_ajout_faculte.setTitle(QCoreApplication.translate("MainWindow", u"Ajout une Facult\u00e9", None))
        self.label_nom_faculte.setText(QCoreApplication.translate("MainWindow", u"Nom de la facult\u00e9:", None))
        self.lineEdit_nom_faculte.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom complet de la facult\u00e9", None))
        self.label_universite_faculte.setText(QCoreApplication.translate("MainWindow", u"Universit\u00e9:", None))
        self.comboBox_universite_faculte.setPlaceholderText(QCoreApplication.translate("MainWindow", u"-- Choisir l'universit\u00e9 --", None))
        self.label_code_faculte.setText(QCoreApplication.translate("MainWindow", u"Code de la facult\u00e9:", None))
        self.lineEdit_code_faculte.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Code unique pour la facult\u00e9", None))
        self.label_nbEtudiants_faculte.setText(QCoreApplication.translate("MainWindow", u"Nombre d'\u00e9tudiants:", None))
        self.lineEditl_nbEtudiants_faculte.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_AjouterFaculte.setText(QCoreApplication.translate("MainWindow", u"Ajouter Facult\u00e9", None))
    # retranslateUi

