## DEPENDECIES-------------------------

# Allow a fucntion to depend on another fucntion
# implementation is in dependency_injection.py module



# ------------------------------------------------------------------------------------------------------
# Component              | What it Means                   | Why it is Used
# ---------------------------------------------------------------
# create_engine          | Creates DB connection engine     | To talk to the database
# declarative_base()     | Base class for ORM models        | Required for model/table creation
# sessionmaker           | Factory for sessions             | Used for DB read/write operations
# SQLALCHEMY_DATABASE_URL| DB connection string             | Tells SQLAlchemy which DB to connect to
# engine                 | Main DB connection               | Executes SQL and manages connections
# connect_args           | SQLite thread config             | Allows FastAPI multithreading
# SessionLocal           | Session generator                | Used per-request DB session
# Base                   | ORM base class                   | All models inherit from it
# ---------------------------------------------------------------

# DATABASE CHECKLIST:
# 1. db definition === database.py  (LIKE conn)
# 2. model definition === model.py  (table structure LIKE CREATE)
# 3. create databse === main.py      (cmd to create table LIKE cur)
# 4. schema definition === schema.py (INPUT AND OUTPUT formating,conversion and validation using pydanci's BaseModel)
# 5. ORM functionality === db_user.py (all funcitonallity LIKE create user)
# 6. API functionality === user.py  (expose to routers )


# Process review

#   Import required libraries: sqlalchemy, passlib, bcrypt
#   Create database definition and run it in main.py
#   Create database models (tables)
#   Create functionality to write to database
#   Create schemas
#          Data from user: UserBase
#          Response to user: UserDisplay

# Create API operation

# SQL is executed only when you call a fetching method like:

# .first()
# .all()
# .one()
# .get()
# .count()