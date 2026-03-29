import logging
import os

# Configuration basique du logging
logging.basicConfig(
    filename='logs/pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def fetch_raw_data():
    """Simule la récupération de données brutes."""
    logging.info("Démarrage de l'extraction des données...")
    # Simulation d'un dictionnaire de données
    data = {"id": 1, "value": "sample_data", "timestamp": "2023-10-27T10:00:00Z"}
    logging.info("Données récupérées avec succès.")
    return data

def transform_data(data):
    """Transforme les données pour Metabase."""
    logging.info("Transformation des données en cours...")
    # TODO: Ajouter une validation de schéma ici
    return data

if __name__ == "__main__":
    raw_data = fetch_raw_data()
    clean_data = transform_data(raw_data)
    print(f"Prêt pour Metabase : {clean_data}")
