from model.contact import Contact
from model.contact_category import ContactCategory    
from base import Session, engine, Base


class ContactExtraction:
    def __init__(self) -> None:
        self._session = Session()


    def getAllContact(self):
        contacts = self.session.query(Contact).all()
        contact_list = []
        for person in contacts:
            # contact_dict = {'contact_id':''}
            print(person.contact_id)
            print(person.contact_name)
            print(person.email_id)
            print(person.whatsapp_no)

    def getAllContactCategory(self):
        contacts_categories = self.session.query(ContactCategory).all()
        contact_category_list = []
        for contact_category in contacts_categories:
            pass

    def getAllContactInfoWithCategoryPriority(self):
        df_contact = self.getAllContact()
        df_contact_category = self.getAllContactCategory()
        # join contact and category on the basis of contact_id and get the complete information
        df_contact_info_with_category = None
        return df_contact_info_with_category

    def getSpecificContactInfoWithCategoryPriority():
        pass

if __name__ == '__main__':
    pass



# 2 - extract a session
# session = Session()

# 3 - extract all movies
# contacts = session.query(Contact).all()

#    contact_id = Column(Integer, primary_key=True)
#     contact_name = Column(String)
#     email_id = Column(String)
#     whatsapp_no = Column(String)

# for person in contacts:
#     print(person.contact_id)
#     print(person.contact_name)
#     print(person.email_id)
#     print(person.whatsapp_no)


