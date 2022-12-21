import sqlite3
from datetime import datetime
from config import app, db
from models import Person, Note
conn = sqlite3.connect("people.db")

columns = [
    "id INTEGER PRIMARY KEY",
    "lname VARCHAR UNIQUE",
    "fname VARCHAR",
    "timestamp DATETIME"
]

# drop_table_cmd = f"DROP TABLE person"
# create_table_cmd = f"CREATE TABLE person ({','.join(columns)})"
# conn.execute(drop_table_cmd)
# conn.execute(create_table_cmd)

people = [
     "1, 'Fairy', 'Tooth', '2022-10-08 09:15:10'",
     "2, 'Ruprecht', 'Knecht', '2022-10-08 09:15:13'",
     "3, 'Bunny', 'Easter', '2022-10-08 09:15:27'",
     "4, 'Banerjee', 'Kaushik', '2022-12-18 09:32:27'",
     "5, 'Unknown', 'Unknown', '2022-12-18 09:32:27'",
]

PEOPLE_NOTES = [
    {
        "lname": "Fairy",
        "fname": "Tooth",
        "notes": [
            ("I brush my teeth after each meal.", "2022-01-06 17:10:24"),
            ("The other day a friend said, I have big teeth.", "2022-03-05 22:17:54"),
            ("Do you pay per gram?", "2022-03-05 22:18:10"),
        ],
    },
    {
        "lname": "Ruprecht",
        "fname": "Knecht",
        "notes": [
            ("I swear, I'll do better this year.", "2022-01-01 09:15:03"),
            ("Really! Only good deeds from now on!", "2022-02-06 13:09:21"),
        ],
    },
    {
        "lname": "Bunny",
        "fname": "Easter",
        "notes": [
            ("Please keep the current inflation rate in mind!", "2022-01-07 22:47:54"),
            ("No need to hide the eggs this time.", "2022-04-06 13:03:17"),
        ],
    },
     {
        "lname": "Banerjee",
        "fname": "Kaushik",
        "notes": [
            ("Please keep practising Python!", "2022-12-19 22:47:54"),
            ("And keep an eye on ur AWS and IaC etc.", "2022-12-20 13:03:17"),
        ],
    },
]
# cursor = conn.cursor()
# for person in people:
#     insert_cmd = f"INSERT INTO person(id, lname, fname, timestamp) \
#     VALUES ({person})"
#     print(insert_cmd)
#     conn.execute(insert_cmd)
#     conn.commit()
# select_cmd = "SELECT * FROM person"  
# print(cursor.fetchall())


with app.app_context():
    db.drop_all()
    db.create_all()
    for data in PEOPLE_NOTES:
        new_person = Person(lname=data.get("lname"), fname=data.get("fname"))
        for content, timestamp in data.get("notes", []):
            new_person.notes.append(
                Note(
                    content=content,
                    timestamp=datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
                )
            )
        db.session.add(new_person)
    db.session.commit()


