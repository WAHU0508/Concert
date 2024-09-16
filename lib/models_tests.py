import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Band, Concert, Venue, session


# band1 = session.query(Band).first()
# band2 = session.query(Band).filter_by(id = 2).first()
# band3 = session.query(Band).filter_by(id = 3).first()
# band4 = session.query(Band).filter_by(id = 4).first()
# band5 = session.query(Band).filter_by(id = 5).first()

# venue1 = session.query(Venue).first()
# venue2 = session.query(Venue).filter_by(id = 2).first()
# venue3 = session.query(Venue).filter_by(id = 3).first()
# venue4 = session.query(Venue).filter_by(id = 4).first()
# venue5 = session.query(Venue).filter_by(id = 5).first()

# concert1 = session.query(Concert).first()
# concert2 = session.query(Concert).filter_by(id = 2).first()
# concert3 = session.query(Concert).filter_by(id = 3).first()
# concert4 = session.query(Concert).filter_by(id = 4).first()
# concert5 = session.query(Concert).filter_by(id = 5).first()

def clean_session():
    yield
    session.rollback()

def test_band_concerts():
    """Test if the the method returns the concerts for a band."""
    band = session.query(Band).filter_by(name = "The Rolling Stones").first()
    concerts = band.concerts()
    assert len(concerts) == 2
    assert concerts[0].venue().title == "Wembley Stadium"
    assert concerts[1].venue().title == "Wembley Stadium"

# def test_band_venues():
#     """Test if the the method returns the concerts for a band."""
#     venues = band2.venues()
#     for venue in venues:
#         assert venue in session.query(Venue).all()
#         for ven in venue.concerts():
#             ven.venue_id == 2

def test_play_in_venue():
    """Test that a new concert for the band is added."""
    band = session.query(Band).filter_by(name = "The Beatles").first()
    venue = session.query(Venue).filter_by(title = "The Forum").first()
    band.play_in_venue(venue, '2024-12-21')
    concert = session.query(Concert).filter_by(band_id = band.id, venue_id = venue.id, date = '2024-12-21').first()
    assert concert is not None
    assert concert.venue().title == "The Forum"
    assert concert.band().name == "The Beatles"

def test_most_performances():
    """Test band with the most performances"""
    the_band = Band.most_performances() 
    assert the_band.name == "The Beatles"

def test_venue_concerts():
    """Test if the the method returns the concerts being held in a venue."""
    venue = session.query(Venue).filter_by(title = "Madison Square Garden").first()
    concerts = venue.concerts()
    assert len(concerts) == 2
    assert concerts[0].band().name == "Led Zeppelin"
    assert concerts[1].band().name == "Queen" 

"""Venue Class Tests"""
def test_concert_on():
    """Test to get a concert being performed on a specified date."""
    venue = session.query(Venue).filter_by(title = "Madison Square Garden").first()
    concert = venue.concert_on('2024-11-04')
    assert concert is not None
    assert concert.band().name == "Led Zeppelin", "Queen"

def test_most_frequent_band():
    venue = session.query(Venue).filter_by(title = "Madison Square Garden").first()
    most_frequent = venue.most_frequent_band()

    assert most_frequent.name == "Led Zeppelin", "Queen"

"""Concert Class Tests"""
def test_hometown_show():
    concert = session.query(Concert).filter_by(date = "2024-09-21").first()
    assert concert.hometown_show() is True
    concert = session.query(Concert).filter_by(date = "2024-12-10").first()
    assert concert.hometown_show() is False

def test_concert_introduction():
    """Test all introductions"""
    concert = session.query(Concert).filter_by(date = "2024-09-21").first()
    intro = concert.introduction()
    assert intro == "Hello London!!!!! We are The Rolling Stones and we're from London"

