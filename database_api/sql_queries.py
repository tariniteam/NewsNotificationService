from contact import Contact
from contact_category import ContactCategory    
from base import Session, engine, Base


# 2 - extract a session
session = Session()

# 3 - extract all movies
contacts = session.query(Contact).all()

#    contact_id = Column(Integer, primary_key=True)
#     contact_name = Column(String)
#     email_id = Column(String)
#     whatsapp_no = Column(String)

for person in contacts:
    print(person.contact_id)
    print(person.contact_name)
    print(person.email_id)
    print(person.whatsapp_no)


