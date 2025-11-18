from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError


from core.guitars.guitars import Guitar

class GuitarRepository:
    def __init__(self, session: Session):
        self.session_internal = session

    def get_by_id(self, guitar_id: int) -> Guitar:
        return self.session_internal.query(Guitar).filter_by(id=guitar_id).first()
    
    def get_by_name(self, guitar_name: str) -> Guitar:
        return self.session_internal.query(Guitar).filter_by(name=guitar_name).first()
    
    def get_all(self) -> List[Guitar]:
        return self.session_internal.query(Guitar).all()
    
    def add(self, guitar: Guitar) -> Guitar:
        try:
            self.session_internal.add(guitar)
            self.session_internal.flush()
            self.session_internal.commit()
            return guitar
        except IntegrityError as e:
            self.session_internal.rollback()
            print(f"Error adding guitar {e}")
            return None
        except Exception as ex:
            self.session_internal.rollback()
            raise
    
    def update(self, guitar: Guitar) -> Guitar:
        try:
            self.session_internal.merge(guitar)
            self.session_internal.flush()
            self.session_internal.commit()
            return guitar
        except IntegrityError:
            self.session_internal.rollback()
            return None
    
    def delete(self, guitar_id: int) -> None:
        guitar_from_db = self.get_by_id(guitar_id)
        if guitar_from_db:
            self.session_internal.delete(guitar_from_db)
            self.session_internal.flush()
            self.session_internal.commit()
            print(f'Gitara {guitar_from_db} uspjesno izbrisana')
        else:
            return None
