import sqlalchemy 
from base import Base


class Contact(Base):
    __tablename__ = 'Contact'

    contact_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    contact_name = sqlalchemy.Column(sqlalchemy.String)
    email_id = sqlalchemy.Column(sqlalchemy.String)
    whatsapp_no = sqlalchemy.Column(sqlalchemy.String)

    def __init__(self, contact_id, contact_name, email_id, whatsapp_no):
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.email_id = email_id
        self.whatsapp_no = whatsapp_no