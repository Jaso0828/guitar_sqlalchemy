from core.guitars.guitars import Guitar
from core.guitars.guitar_categories import GuitarCategory
from core.guitars.guitar_types import GuitarType
from .database.database import Base, engine, get_session
from infrastructures.guitars.guitar_repo import GuitarRepository
from infrastructures.guitars.guitar_type_repo import GuitarTypeRepository
from infrastructures.guitars.guitar_category_repo import GuitarCategoryRepository
from config import GUITAR_CATEGORIES, GUITAR_TYPES

class BaseRepository:
    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = get_session()

        self.guitar_repo = GuitarRepository(self.session)
        self.guitar_type_repo = GuitarTypeRepository(self.session)
        self.guitar_category_repo = GuitarCategoryRepository(self.session)

    

    def db_seed(self):
        for guitar_category in GUITAR_CATEGORIES:
            self.guitar_category_repo.add(GuitarCategory(name=guitar_category))
        
        for guitar_type in GUITAR_TYPES:
            self.guitar_type_repo.add(GuitarType(name=guitar_type))