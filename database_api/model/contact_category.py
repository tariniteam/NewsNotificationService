from sqlalchemy import Column, String, Integer, Date
from base import Base


class ContactCategory(Base):
    __tablename__ = 'ContactCategory'

    contact_category_id = Column(Integer,primary_key=True)
    contact_id = Column(Integer)
    category = Column(String)
    sub_category = Column(String)
    priority = Column(String)

    def __init__(self, contact_category_id, contact_id, category, sub_category, priority):
        self.contact_category_id = contact_category_id
        self.contact_id = contact_id
        self.category = category
        self.sub_category = sub_category
        self.priority = priority