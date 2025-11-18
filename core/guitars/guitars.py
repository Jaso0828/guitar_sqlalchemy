from typing import List
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship

from infrastructures.database.database import Base
from config import NAME_LENGHT, DESCRIPTION_LENGHT, URL_LENGHT, LOCATIONS_STR

class Guitar(Base):
    __tablename__ = 'guitars'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(NAME_LENGHT), nullable=False)
    year = Column(Integer, nullable=False)
    price = Column(DECIMAL, nullable=False)

    description = Column(String(DESCRIPTION_LENGHT), nullable=True)
    image_url = Column(String(URL_LENGHT), nullable=True)
    location = Column(String(LOCATIONS_STR), nullable=True)

    guitar_type_id = Column(Integer, ForeignKey('guitar_type.id'))
    guitar_category_id = Column(Integer, ForeignKey('guitar_category.id'))

    guitar_type = relationship('GuitarType', back_populates='guitars')
    guitar_category = relationship('GuitarCategory', back_populates='guitars')
    

    def __repr__(self):
        if self.id:
            return f'Guitar: {self.id} - {self.name} - {self.price:.2f} EUR'
        else:
            return f'Guitar: {self.name} - {self.price:.3f} EUR'