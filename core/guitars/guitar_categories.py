from typing import List
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship

from infrastructures.database.database import Base
from config import NAME_LENGHT

class GuitarCategory(Base):
    __tablename__ = 'guitar_category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(NAME_LENGHT), nullable=False)

    guitars = relationship('Guitar', back_populates='guitar_category')

    def __repr__(self):
        return f"Guitar category: {self.name}"