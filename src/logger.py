import logging
import os
from datetime import datetime

# Création d'un nom de fichier de log avec date et heure actuelles, format : mm_jj_aaaa_hh_mm_ss.log
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Construction du chemin vers un dossier 'logs' dans le répertoire de travail courant
logs_path = os.path.join(os.getcwd(), "logs")

# Création du dossier 'logs' s'il n'existe pas déjà (évite une erreur si le dossier existe)
os.makedirs(logs_path, exist_ok=True)

# Chemin complet vers le fichier log qui sera créé dans ce dossier
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configuration du module logging Python
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Fichier où seront écrits les logs
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Format des messages de log
    level=logging.INFO  # Niveau minimum des logs à enregistrer (INFO et plus grave)
)