from sqlalchemy import Column, String, Integer, Date

from base import Base


class Contact(Base):
    __tablename__ = 'Contact'

    contact_id = Column(Integer, primary_key=True)
    contact_name = Column(String)
    email_id = Column(String)
    whatsapp_no = Column(String)

    def __init__(self, contact_id, contact_name, email_id, whatsapp_no):
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.email_id = email_id
        self.whatsapp_no = whatsapp_no