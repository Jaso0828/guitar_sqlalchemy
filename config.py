DATABASE_PATH = "sqlite:///data_store/db/guitars.db"

# Models constants
NAME_LENGHT = 150
DESCRIPTION_LENGHT = 1500
URL_LENGHT = 450
LOCATIONS_STR = 50

GUITAR_CATEGORIES = ["Acoustic", "Electric", "Bass"]
GUITAR_TYPES = ["Clasical", "Steel-string acoustuc", "Resonator guitar", "Solid-body electric", "Semi-hollow/hollow body electric", "Acoustic-electric", "Bariton guitar", "Electric bass", "Acoustic bass"]

class AppConfig:
    def __init__(self, db_path = DATABASE_PATH):
        self.db_path = db_path