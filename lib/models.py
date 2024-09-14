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

band_venue = Table(
    'band_venues',
    Base.metadata,
    Column('band_id', ForeignKey('bands.id'), primary_key=True),
    Column('venue_id', ForeignKey('venues.id'), primary_key=True),
    extend_existing=True,
)

class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    hometown = Column(String())

    """One to many relationship between band and concerts"""
    all_concerts = relationship('Concert', backref=backref('my_band'))

    """Many to many relationship between band and venue using table objects"""
    all_venues = relationship('Venue', secondary=band_venue, back_populates='all_bands')

    def concerts(self):
        return self.all_concerts

    def venues(self):
        return self.all_venues
    
    def __repr__(self):
        return f'<Band: id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'home_town={self.hometown}>'

    

class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    city = Column(String())

    """One to many relationship between band and concerts"""
    all_concerts = relationship('Concert', backref = backref('my_venue'))

    """Many to many relationship between band and venue using table objects"""
    all_bands = relationship('Band', secondary=band_venue, back_populates='all_venues')
    
    def concerts(self):
        return self.all_concerts
    
    def bands(self):
        return self.all_bands
    
    def __repr__(self):
        return f'<Venue: id={self.id}, ' + \
            f'title={self.title}, ' + \
            f'city={self.city}>'

class Concert(Base):
    __tablename__ = 'concerts'

    id = Column(Integer(), primary_key=True)
    date = Column(String())

    band_id = Column(Integer(), ForeignKey('bands.id'))
    venue_id = Column(Integer(), ForeignKey('venues.id'))

    def band(self):
        return self.my_band
    
    def venue(self):
        return self.my_venue
    
    def hometown_show(self):
        return self.venue.city == self.band.hometown
    
    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
    
    def __repr__(self):
        return f'<Concert: id={self.id}, ' + \
            f'date={self.date}, ' + \
            f'band_id={self.band_id}, ' + \
            f'venue_id={self.venue_id}>'