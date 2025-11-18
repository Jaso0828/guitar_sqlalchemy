from typing import List
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship

from infrastructures.database.database import Base
from config import NAME_LENGHT


class GuitarType(Base):
    __tablename__ = 'guitar_type'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(NAME_LENGHT), nullable=False)

    guitars = relationship('Guitar', back_populates='guitar_type')

    def __repr__(self):
        return f"Guitar type: {self.name}"