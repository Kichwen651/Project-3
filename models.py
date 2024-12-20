from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    preferred_style = Column(String)
    
    # Define a relationship to Service (One-to-many)
    services = relationship("Service", back_populates="client")

    def __repr__(self):
        return f"Client(id={self.id}, name={self.name}, email={self.email}, phone_number={self.phone_number}, preferred_style={self.preferred_style})"

class Artist(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    specialization = Column(String)
    contact_info = Column(String)
    
    # Define a relationship to Service (One-to-many)
    services = relationship("Service", back_populates="artist")

    def __repr__(self):
        return f"Artist(id={self.id}, name={self.name}, specialization={self.specialization}, contact_info={self.contact_info})"

class Service(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    cost = Column(Integer)
    client_id = Column(Integer, ForeignKey('clients.id'))
    artist_id = Column(Integer, ForeignKey('artists.id'))
    
    # Define relationships to Client and Artist (Many-to-one)
    client = relationship("Client", back_populates="services")
    artist = relationship("Artist", back_populates="services")

    def __repr__(self):
        return f"Service(id={self.id}, description={self.description}, cost={self.cost}, client_id={self.client_id}, artist_id={self.artist_id})"

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey('services.id'))
    amount = Column(Integer)
    payment_status = Column(String)
    transaction_date = Column(String)
    
    # Define relationship to Service (Many-to-one)
    service = relationship("Service")

    def __repr__(self):
        return f"Transaction(id={self.id}, service_id={self.service_id}, amount={self.amount}, payment_status={self.payment_status}, transaction_date={self.transaction_date})"

# Set up the engine (usually in the main app or where you create the session)
engine = create_engine('sqlite:///./yourdatabase.db')  # Use the correct database URL

# Create all tables in the database (if not already created)
Base.metadata.create_all(engine)
