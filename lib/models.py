from sqlalchemy import ForeignKey, Table, Column, Integer, String, MetaData, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

engine = create_engine('sqlite:///concerts.db')
Session = sessionmaker(bind=engine)
session = Session()

class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    hometown = Column(String())

    """One to many relationship between band and concerts"""
    concerts = relationship('Concert', backref = backref('bands'))

    def __repr__(self):
        return f'Band(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'home_town={self.hometown})'
    
class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    city = Column(String())

    """One to many relationship between band and concerts"""
    concerts = relationship('Concert', backref = backref('venues'))

    def __repr__(self):
        return f'<Venue: id={self.id}, ' + \
            f'tilte={self.title}, ' + \
            f'city={self.city}>'

class Concert(Base):
    __tablename__ = 'concerts'

    id = Column(Integer(), primary_key=True)
    date = Column(String())

    band_id = Column(Integer(), ForeignKey('bands.id'))
    venue_id = Column(Integer(), ForeignKey('venues.id'))