import sys
import logging
import os
from datetime import datetime

def get_error_details(error_message, error_detail: sys):
    """
    Retourne un message d'erreur enrichi avec le nom du fichier et le numéro de ligne.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    return f"Erreur dans le fichier : {file_name}, à la ligne {line_number} -> {error_message}"

class CustomException(Exception):
    """
    Classe personnalisée pour afficher les erreurs avec plus de détails.
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = get_error_details(error_message, error_detail)

    def __str__(self):
        return self.error_message

# Configuration du logging
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)