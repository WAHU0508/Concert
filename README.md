### Sharon Gikenye's Code Challenge
Phase-3 Week-3 Code Challenge

For this assignment, we'll be working with a Concert domain.

We have three models: Band(name and hometown),Venue(title and city), and Concert.

For our purposes, a Band has many Concerts, a Venue has many Concerts, 
and a Concert belongs to a Band and to a Venue.

Band - Venue is a many to many relationship.
Band - Concert is s one to many relationship.
Venue - Concert is a one to many relationship.
Our single source of truth is concert

Topics
SQLAlchemy Migrations
SQLAlchemy Relationships
Class and Instance Methods
SQLAlchemy Querying
 
## Setup
1. cd into lib then create a migration environment by running:
    ``` bash
        alembic init migrations
    ```
    In [alembic.ini](./lib/alembic.ini) have sqlalchemy.url = sqlite:///concerts.db
    Then configure our database in [models.py](./lib/models.py)
    Configure [envy.py](./lib/migrations/env.py):
    ``` bash
        from models import Base
        target_metadata = Base.metadata
    ```
    Then finally you can generate your first migration:
    ``` bash
        alembic revision -m "Empty Init"
        alembic upgrade head
    ```
2. Create schema for the bands table and Concerts table:
   What You Should Have:
   Your schema should look like this:
 

* Bands Table

| Column | Type |
|-----|----|
|name| String|

|hometown | String|

* venues Table

| Column | Type |
|--------|-------|
| title | String |
| city | String |

After creating the bands and venues schema, generate migrations.

You will need to create a schema for the concerts table using the attributes specified in the deliverables below. 

You will also need to create the migrations for the above tables using the attributes specified in the deliverables below

Deliverables
Write the following methods in the classes you will write. Feel free to build out any helper methods if needed.

Remember: SQLAlchemy gives your classes access to a lot of methods already! Keep in mind what methods SQLAlchemy gives you access to on each of your classes when you're approaching the deliverables below.

Migrations
Before working on these deliverables, you will need to create migrations for the concerts  tables. This is assuming you had already created and migrated the band and venues table above.

A Concert belongs to a Band, and a Concert also belongs to a Venue. In your migration, create any columns your concerts table will need to establish these relationships.
The concerts table should also have:
A date column that stores an string.
After creating the concerts table using a migration, create instances of your classes so you can test your code.

Once you've set up your tables, work on building out the following deliverables.
