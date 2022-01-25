from pydantic import BaseModel


class Record(BaseModel):

    id = int
    day = str
    w_l = str
    ot = str
    rec = str
    location = str
    opp = str
    TeamPoints = int
    OppPoints = int
    Firsts = int
    TotYdO = int
    PassYO = int
    RushYO = int
    TeamTOs = int
    FirstsA = int
    TotYdA = int
    PassYA = int
    RushYA = int
    ForcedTOs = int
    Week = int

    class Config:
        orm_mode = True
