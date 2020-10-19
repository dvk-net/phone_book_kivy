from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///phones.sqlite', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phones = relationship("Phone", cascade="all,delete", back_populates="user")

    def __str__(self):
        return self.name
    
    @classmethod
    def add(cls, name): 
        user = cls(name=name)
        session.add(user)
        session.commit()
        return user

    @classmethod
    def delete_by_id(cls, id): 
        user = session.query(cls).filter_by(id=id).first()
        if user:
            session.delete(user)
            session.commit()
            return True
        return False
    @classmethod
    def all(cls): 
        return session.query(cls).all()

    @classmethod
    def find_by_name(cls, name): 
        return session.query(cls).filter(cls.name.ilike(f'%{name}%'))

    @classmethod
    def find_by_phone(cls, phone):
        return session.query(cls).join(Phone).filter(Phone.phone.ilike(f'%{phone}%'))


class Phone(Base):
    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True)
    phone = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="phones")

    def __str__(self):
        return self.phone

    @classmethod
    def add(cls, phone, user):
        phone = cls(phone=phone, user=user)
        session.add(phone)
        session.commit()
        return phone


Base.metadata.create_all(engine)