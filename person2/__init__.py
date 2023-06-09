
from person2 import db, model
# import db
# import model

def read_person(name):
    session = db.getSession()
    person = session.query(model.Person).filter_by(name=name).first()
    session.close()
    return person