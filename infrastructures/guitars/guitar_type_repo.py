from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError


from core.guitars.guitar_types import GuitarType

class GuitarTypeRepository:
    def __init__(self, session: Session):
        self.session_internal = session

    def get_by_id(self, guitar_type_id: int) -> GuitarType:
        return self.session_internal.query(GuitarType).filter_by(id=guitar_type_id).first()
    
    def get_by_name(self, guitar_type_name: str) -> GuitarType:
        return self.session_internal.query(GuitarType).filter_by(name=guitar_type_name).first()
    
    def get_all(self) -> List[GuitarType]:
        return self.session_internal.query(GuitarType).all()
    
    def add(self, guitar_type: GuitarType) -> GuitarType:
        try:
            self.session_internal.add(guitar_type)
            self.session_internal.flush()
            self.session_internal.commit()
            return guitar_type
        except IntegrityError as e:
            self.session_internal.rollback()
            print(f"Error adding guitar {e}")
            return None
        except Exception as ex:
            self.session_internal.rollback()
            raise
    
    def update(self, guitar_type: GuitarType) -> GuitarType:
        try:
            self.session_internal.merge(guitar_type)
            self.session_internal.flush()
            self.session_internal.commit()
            return guitar_type
        except IntegrityError:
            self.session_internal.rollback()
            return None
    
    def delete(self, guitar_type_id: int) -> None:
        guitar_type_from_db = self.get_by_id(guitar_type_id)
        if guitar_type_from_db:
            self.session_internal.delete(guitar_type_from_db)
            self.session_internal.flush()
            self.session_internal.commit()
            print(f'Gitara {guitar_type_from_db} uspjesno izbrisana')
        else:
            return None
