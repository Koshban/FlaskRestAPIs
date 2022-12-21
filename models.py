from datetime import datetime
from config import ma, db
from marshmallow_sqlalchemy import fields

""" Note Class as the child class/child table for person with a 1-2-many relationship 
b/w person-Notes"""
class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    content = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        load_instance = True
        sqla_session = db.session
        include_fk = True

""" Persdon Class using db.model initiated in config.py. This will help to convert the Data in table into Pythonic Objects"""

class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), unique=True)
    fname = db.Column(db.String(32), unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    notes = db.relationship(
        Note, 
        backref="person", 
        cascade="all, delete, delete-orphan", 
        single_parent=True,   
        order_by="desc(Note.timestamp)"
    )

""" PersonSchema to use Marhmallow to serialize/De-Serialize the Python Objects created by person class above."""
"""For PersonSchema, the model is Person, and sqla_session is db.session. This is how Marshmallow finds 
attributes in the Person class and learns the types of those attributes so it knows how to serialize and deserialize them."""

class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person  # So that it knows to look in person class above
        load_instance = True  # deserialize JSON data and load Person model instances from it.
        sqla_session = db.session  # So that it knows what datatype schema it is looking for in person class
        include_relationships = True  # To include Notes Table
    
    notes = fields.Nested(NoteSchema, many=True)
    
    
note_schema = NoteSchema()
person_schema = PersonSchema()
people_schema = PersonSchema(many=True)

