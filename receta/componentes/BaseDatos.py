from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "oracle+cx_oracle://CR:CR@XE",
    max_identifier_length=128)

Session = sessionmaker(bind=engine)

session = Session()

from datetime import datetime

from sqlalchemy import (Table, Column, \
                        Integer, Numeric, String, DateTime \
    , ForeignKey, Boolean, select, insert, update, delete)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class RecetaHe1(Base):
    __tablename__ = "RECETA_HE1"
    id = Column(Integer, primary_key=True)
    archivo = Column(String(200), nullable=True)
    enviado = Column(Integer, nullable=True, default=0)
    email = Column(String(200), nullable=True, default='christian19782013@gmail.com')

    def __init__(self, archivo):
        self.archivo = archivo

    def __repr__(self):
        return 'RecetaHe1{self.id}'.format(self=self)
