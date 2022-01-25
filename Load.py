import csv
import datetime
import Models
from Database import SessionLocal, engine

db = SessionLocal()

Models.Base.metadata.create_all(bind=engine)

with open("gnb_2018.csv", "r") as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        db_record = Models.Record(
            day=row["day"],
            w_l = row["w_l"],
            ot = row["ot"],
            rec = row["rec"],
            location = row["location"],
            opp = row["opp"],
            TeamPoints = row["TeamPoints"],
            OppPoints = row["OppPoints"],
            Firsts = row["Firsts"],
            TotYdO = row["TotYdO"],
            PassYO = row["PassYO"],
            RushYO = row["RushYO"],
            TeamTOs = row["TeamTOs"],
            FirstsA = row["FirstsA"],
            TotYdA = row["TotYdA"],
            PassYA = row["PassYA"],
            RushYA = row["RushYA"],
            ForcedTOs = row["ForcedTOs"],
            Week = row["Week"],
        )
        db.add(db_record)

    db.commit()

db.close()
