from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from core.guitars.guitar_categories import GuitarCategory

class GuitarCategoryRepository:
    def __init__(self, session: Session):
        self.session_internal = session

    def get_by_id(self, guitar_category_id: int) -> GuitarCategory:
        return self.session_internal.query(GuitarCategory).filter_by(id=guitar_category_id).first()

    def get_by_name(self, guitar_category_name: str) -> GuitarCategory:
        return self.session_internal.query(GuitarCategory).filter_by(name=guitar_category_name).first()

    def add(self, guitar_category: GuitarCategory) -> GuitarCategory:
        try:
            self.session_internal.add(guitar_category)
            self.session_internal.flush()
            self.session_internal.commit()
            return guitar_category
        except IntegrityError as e:
            self.session_internal.rollback()
            return None
        
    def update(self, guitar_category: GuitarCategory) -> GuitarCategory:
        try:
            guitar_category_from_db = self.get_by_id(guitar_category.id)
            if guitar_category_from_db:
                guitar_category_from_db = guitar_category
                self.session_internal.flush()
                self.session_internal.commit()
                return guitar_category_from_db
        except IntegrityError:
            self.session_internal.rollback()
            return None
        
    def delete(self, guitar_category_id: int):
        guitar_category_from_db = self.get_by_id(guitar_category_id)
        if guitar_category_id:
            self.session_internal.delete(guitar_category_from_db)
            self.session_internal.commit()
        else:
            return None