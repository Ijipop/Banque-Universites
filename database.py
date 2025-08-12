from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Configuration de la base de données
engine = create_engine("sqlite:///universites_facultes.db", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Universite(Base):
    __tablename__ = "universites"
    
    id = Column(Integer, primary_key=True)
    nom = Column(String(150), unique=True, nullable=False)
    ville = Column(String(100), nullable=False)
    code_universite = Column(String(10), unique=True, nullable=False)
    annee_fondation = Column(Integer, nullable=True)
    
    # Relation 1-à-N : Une université a plusieurs facultés
    # cascade="all, delete-orphan" : si on supprime une université, ses facultés sont supprimées
    facultes = relationship("Faculte", back_populates="universite", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Universite(id={self.id}, nom='{self.nom}', ville='{self.ville}', code='{self.code_universite}')>"

class Faculte(Base):
    __tablename__ = "facultes"
    
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    code_faculte = Column(String(10), nullable=False)
    nombre_etudiants = Column(Integer, default=0)
    
    # Clé étrangère obligatoire vers l'université
    universite_id = Column(Integer, ForeignKey("universites.id"), nullable=False)
    
    # Relation inverse : Une faculté appartient à une université
    universite = relationship("Universite", back_populates="facultes")
    
    def __repr__(self):
        return f"<Faculte(id={self.id}, nom='{self.nom}', code='{self.code_faculte}', etudiants={self.nombre_etudiants}, universite_id={self.universite_id})>"

# Création des tables
Base.metadata.create_all(engine)

def initialiser_donnees():
    """Initialise quelques données de base si la base est vide"""
    
    # Vérifier si des données existent déjà
    if session.query(Universite).count() > 0:
        print("Les données existent déjà.")
        return
    
    print("Initialisation des données de base...")
    
    # Créer les universités
    universites_donnees = [
        {"nom": "Université de Montréal", "ville": "Montréal", "code": "UdeM", "annee": 1878},
        {"nom": "UQAM", "ville": "Montréal", "code": "UQAM", "annee": 1969},
        {"nom": "Université Laval", "ville": "Québec", "code": "UL", "annee": 1663},
        {"nom": "Concordia University", "ville": "Montréal", "code": "CONC", "annee": 1974},
    ]
    
    universites_objets = []
    for data in universites_donnees:
        universite = Universite(
            nom=data["nom"], 
            ville=data["ville"], 
            code_universite=data["code"], 
            annee_fondation=data["annee"]
        )
        universites_objets.append(universite)
        session.add(universite)
    
    # Flush pour obtenir les IDs
    session.flush()
    
    # Créer les facultés pour chaque université
    facultes_donnees = [
        # Université de Montréal (UdeM)
        {"nom": "Faculté de Médecine", "code": "MED", "etudiants": 2500, "universite_code": "UdeM"},
        {"nom": "Faculté de Génie", "code": "GENIE", "etudiants": 1800, "universite_code": "UdeM"},
        {"nom": "Faculté de Droit", "code": "DROIT", "etudiants": 1200, "universite_code": "UdeM"},
        
        # UQAM
        {"nom": "École des Sciences de la Gestion", "code": "ESG", "etudiants": 3000, "universite_code": "UQAM"},
        {"nom": "Faculté des Arts", "code": "ARTS", "etudiants": 1500, "universite_code": "UQAM"},
        {"nom": "Faculté des Sciences", "code": "SCI", "etudiants": 2200, "universite_code": "UQAM"},
        
        # Université Laval (UL)
        {"nom": "Faculté de Médecine", "code": "MED", "etudiants": 2000, "universite_code": "UL"},
        {"nom": "Faculté des Sciences et de Génie", "code": "FSG", "etudiants": 2800, "universite_code": "UL"},
        
        # Concordia University (CONC)
        {"nom": "Gina Cody School of Engineering", "code": "ENG", "etudiants": 2100, "universite_code": "CONC"},
        {"nom": "John Molson School of Business", "code": "BUS", "etudiants": 2600, "universite_code": "CONC"},
    ]
    
    for fac_data in facultes_donnees:
        # Trouver l'université correspondante
        universite = session.query(Universite).filter_by(code_universite=fac_data["universite_code"]).first()
        if universite:
            faculte = Faculte(
                nom=fac_data["nom"],
                code_faculte=fac_data["code"],
                nombre_etudiants=fac_data["etudiants"],
                universite_id=universite.id
            )
            session.add(faculte)
    
    # Sauvegarder tout
    session.commit()
    print(f"Données initialisées : {len(universites_donnees)} universités et {len(facultes_donnees)} facultés")

def ajouter_universite(nom, ville, code_universite, annee_fondation=None):
    """
    Ajoute une nouvelle université
    
    Args:
        nom: Nom de l'université
        ville: Ville de l'université
        code_universite: Code unique de l'université
        annee_fondation: Année de fondation (optionnel)
    
    Returns:
        Universite créée ou None si erreur
    """
    try:
        # Validation des données
        if not nom or not ville or not code_universite:
            print("Erreur : Nom, ville et code sont obligatoires")
            return None
        
        if len(code_universite) > 10:
            print("Erreur : Le code université ne peut pas dépasser 10 caractères")
            return None
        
        if annee_fondation and annee_fondation < 1000:
            print("Erreur : L'année de fondation doit être supérieure à 1000")
            return None
        
        # Vérifier que l'université n'existe pas déjà
        universite_existante = session.query(Universite).filter(
            (Universite.nom == nom) | (Universite.code_universite == code_universite)
        ).first()
        
        if universite_existante:
            print(f"Erreur : Une université avec ce nom ou ce code existe déjà")
            return None
        
        # Créer la nouvelle université
        nouvelle_universite = Universite(
            nom=nom,
            ville=ville,
            code_universite=code_universite,
            annee_fondation=annee_fondation
        )
        
        session.add(nouvelle_universite)
        session.commit()
        
        print(f"Université '{nom}' ajoutée avec succès")
        return nouvelle_universite
        
    except Exception as e:
        session.rollback()
        print(f"Erreur lors de l'ajout de l'université : {e}")
        return None

def ajouter_faculte(nom_faculte, code_faculte, nombre_etudiants, universite_id):
    """
    Ajoute une nouvelle faculté à une université existante
    
    Args:
        nom_faculte: Nom de la faculté
        code_faculte: Code de la faculté
        nombre_etudiants: Nombre d'étudiants
        universite_id: ID de l'université parent
    
    Returns:
        Faculte créée ou None si erreur
    """
    try:
        # Validation des données
        if not nom_faculte or not code_faculte:
            print("Erreur : Nom et code de la faculté sont obligatoires")
            return None
        
        if len(code_faculte) > 10:
            print("Erreur : Le code faculté ne peut pas dépasser 10 caractères")
            return None
        
        if nombre_etudiants < 0:
            print("Erreur : Le nombre d'étudiants doit être positif")
            return None
        
        # Vérifier que l'université existe
        universite = session.query(Universite).filter_by(id=universite_id).first()
        if not universite:
            print(f"Erreur : L'université avec l'ID {universite_id} n'existe pas")
            return None
        
        # Vérifier que la faculté n'existe pas déjà pour cette université
        faculte_existante = session.query(Faculte).filter_by(
            nom=nom_faculte, 
            universite_id=universite_id
        ).first()
        
        if faculte_existante:
            print(f"Erreur : La faculté '{nom_faculte}' existe déjà pour {universite.nom}")
            return None
        
        # Créer la nouvelle faculté
        nouvelle_faculte = Faculte(
            nom=nom_faculte,
            code_faculte=code_faculte,
            nombre_etudiants=nombre_etudiants,
            universite_id=universite_id
        )
        
        session.add(nouvelle_faculte)
        session.commit()
        
        print(f"Faculté '{nom_faculte}' ajoutée avec succès à {universite.nom}")
        return nouvelle_faculte
        
    except Exception as e:
        session.rollback()
        print(f"Erreur lors de l'ajout de la faculté : {e}")
        return None

def obtenir_universites():
    """Retourne toutes les universités triées par nom"""
    return session.query(Universite).order_by(Universite.nom).all()

def obtenir_facultes_par_universite(universite_id):
    """Retourne toutes les facultés d'une université donnée"""
    return session.query(Faculte).filter_by(universite_id=universite_id).order_by(Faculte.nom).all()

def obtenir_facultes_par_code_universite(code_universite):
    """Retourne toutes les facultés d'une université donnée par son code"""
    universite = session.query(Universite).filter_by(code_universite=code_universite).first()
    if universite:
        return obtenir_facultes_par_universite(universite.id)
    return []

def obtenir_statistiques():
    """Retourne les statistiques de la base de données"""
    nb_universites = session.query(Universite).count()
    nb_facultes = session.query(Faculte).count()
    
    return {
        "universites": nb_universites,
        "facultes": nb_facultes
    }

def afficher_toutes_les_donnees():
    """Affiche toutes les données de la base de données"""
    print("\n" + "="*60)
    print("DONNEES COMPLETES DE LA BASE DE DONNEES")
    print("="*60)
    
    # Afficher les statistiques
    stats = obtenir_statistiques()
    print(f"\nSTATISTIQUES :")
    print(f"   - {stats['universites']} universités")
    print(f"   - {stats['facultes']} facultés")
    
    # Afficher toutes les universités avec leurs facultés
    universites = obtenir_universites()
    for univ in universites:
        print(f"\nUNIVERSITE : {univ.nom}")
        print(f"   Ville : {univ.ville}")
        print(f"   Code : {univ.code_universite}")
        if univ.annee_fondation:
            print(f"   Fondée en : {univ.annee_fondation}")
        
        facultes = obtenir_facultes_par_universite(univ.id)
        if facultes:
            print(f"   Facultés ({len(facultes)}):")
            for fac in facultes:
                print(f"      - {fac.nom} ({fac.code_faculte}) - {fac.nombre_etudiants} étudiants")
        else:
            print(f"   Aucune faculté")
    
    print("\n" + "="*60)

# Initialiser les données au démarrage
if __name__ == "__main__":
    initialiser_donnees()
    
    # Afficher toutes les données
    afficher_toutes_les_donnees()
    
    # Exemple d'utilisation spécifique
    print(f"\nEXEMPLE - Facultés de l'Université de Montréal :")
    facultes_udem = obtenir_facultes_par_code_universite("UdeM")
    for fac in facultes_udem:
        print(f"  - {fac.nom} ({fac.code_faculte}) - {fac.nombre_etudiants} étudiants")