#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Band, Venue, Concert

if __name__ == '__main__':
    engine = create_engine('sqlite:///concerts.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Band).delete()
    session.query(Venue).delete()
    session.query(Concert).delete()

    band1 = Band(name = 'The Rolling Stones', hometown = 'London')
    band2 = Band(name = 'The Beatles', hometown = 'Liverpool')
    band3 = Band(name = 'Led Zeppelin', hometown = 'London')
    band4 = Band(name = 'Pink Floyd', hometown = 'Cambridge')
    band5 = Band(name = 'Queen', hometown = 'London')
    session.add_all([band1, band2, band3, band4, band5])
    session.commit()

    venue1 = Venue(title = 'Wembley Stadium', city = 'London')
    venue2 = Venue(title = 'Madison Square Garden', city = 'New York')
    venue3 = Venue(title = 'The Forum', city = 'Los Angeles')
    venue4 = Venue(title = 'Sydney Opera House', city = 'Sydney')
    venue5 = Venue(title = 'Red Rocks Amphitheater', city = 'Denver')
    session.add_all([venue1, venue2, venue3, venue4, venue5])
    session.commit()

    concert1 = Concert(date = '2024-09-15', band_id = band1.id, venue_id = venue1.id)
    concert2 = Concert(date = '2024-10-05', band_id = band2.id, venue_id = venue2.id)
    concert3 = Concert(date = '2024-11-20', band_id = band3.id, venue_id = venue3.id)
    concert4 = Concert(date = '2024-12-10', band_id = band4.id, venue_id = venue4.id)
    concert5 = Concert(date = '2024-01-22', band_id = band5.id, venue_id = venue5.id)
    session.add_all([concert1, concert2, concert3, concert4, concert5])
    session.commit()