#!/usr/bin/env python3

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from models import Band, Venue, Concert

if __name__ == '__main__':
    engine = create_engine('sqlite:///concerts.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Band).delete()
    session.query(Venue).delete()
    session.query(Concert).delete()

    session.execute(text('DELETE FROM band_venues'))

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

    concert101 = Concert(date = '2024-09-15', band_id = band1.id, venue_id = venue1.id)
    concert102 = Concert(date = '2024-09-21', band_id = band1.id, venue_id = venue1.id)
    concert103 = Concert(date = '2024-09-21', band_id = band1.id, venue_id = venue2.id)
    concert201 = Concert(date = '2024-10-05', band_id = band2.id, venue_id = venue1.id)
    concert202 = Concert(date = '2024-10-19', band_id = band2.id, venue_id = venue3.id)
    concert301 = Concert(date = '2024-11-04', band_id = band3.id, venue_id = venue2.id)
    concert302 = Concert(date = '2024-11-31', band_id = band3.id, venue_id = venue3.id)
    concert401 = Concert(date = '2024-12-10', band_id = band4.id, venue_id = venue1.id)
    concert501 = Concert(date = '2024-01-22', band_id = band5.id, venue_id = venue2.id)
    concert502 = Concert(date = '2024-01-07', band_id = band5.id, venue_id = venue3.id)
    session.add_all([concert101, concert102, concert201, concert202, concert301, concert302, concert401, concert501, concert502])
    session.commit()

    band1.all_venues.append(venue1)
    band1.all_venues.append(venue2)
    band2.all_venues.append(venue1)
    band2.all_venues.append(venue3)
    band3.all_venues.append(venue2)
    band3.all_venues.append(venue3)
    band4.all_venues.append(venue1)
    band5.all_venues.append(venue3)
    session.commit()