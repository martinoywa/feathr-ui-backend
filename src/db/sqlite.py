from sqlalchemy import create_engine, Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


SQLALCHEMY_DATABASE_URL = "sqlite:///./feathr.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class ProjectDB(Base):
    __tablename__ = "projects"

    name = Column("name", String, primary_key=True)


class DataSourceAttributesDB(Base):
    __tablename__ = "data_source_attributes"

    id = Column(Integer, primary_key=True, index=True)
    event_timestamp_column = Column("event_timestamp_column", String)
    name = Column(String)
    path = Column(String)
    preprocessing = Column(String)
    qualified_name = Column(String)
    timestamp_format = Column(String)
    type = Column("type", String)
    data_source_id = Column(Integer, ForeignKey('data_sources.id'))

    data_source = relationship("DataSourceDB", back_populates="attributes")


class DataSourceDB(Base):
    __tablename__ = "data_sources"

    id = Column(Integer, primary_key=True, index=True)
    display_text = Column(String)
    guid = Column(String)
    last_modified_ts = Column(String)
    status = Column(String)
    type_name = Column("type_name", String)
    version = Column(String)

    attributes = relationship("DataSourceAttributesDB", back_populates="data_source")

# create tables
Base.metadata.create_all(engine)

# db session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()