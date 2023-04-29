from sqlalchemy import Column, String, Integer, Date

from base import Base

# Contacts Key | Category | Sub Category Choice | Priority 

class ContactCategory(Base):
    __tablename__ = 'ContactCategory'

    contact_category_id = Column(Integer,primary_key=True)
    contact_id = Column(Integer)
    category = Column(String)
    sub_category = Column(String)
    priority = Column(String)

    def __init__(self, contact_category_id, contact_id, category, sub_category, priorty):
        self.contact_category_id = contact_category_id
        self.contact_id = contact_id
        self.category = category
        self.email_id = sub_category
        self.whatsapp_no = priorty