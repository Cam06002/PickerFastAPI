from sqlalchemy import Column, Integer, String
from Database import Base


class Record(Base):
    __tablename__ = "gnb_2018.csv"

    id = Column(Integer, primary_key=True, index=True)
    day = Column(String(255))
    w_l = Column(String(255))
    ot = Column(String(255))
    rec = Column(String(255))
    location = Column(String(255))
    opp = Column(String(255))
    TeamPoints = Column(Integer)
    OppPoints = Column(Integer)
    Firsts = Column(Integer)
    TotYdO = Column(Integer)
    PassYO = Column(Integer)
    RushYO = Column(Integer)
    TeamTOs = Column(Integer)
    FirstsA = Column(Integer)
    TotYdA = Column(Integer)
    PassYA = Column(Integer)
    RushYA = Column(Integer)
    ForcedTOs = Column(Integer)
    Week = Column(Integer)
