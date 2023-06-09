import sys
# sys.path.append('../database_api')
from database_api.model.contact import Contact
from database_api.model.contact_category import ContactCategory    
from database_api.base import Session, engine, Base
import pandas as pd

class ContactExtraction:
    def __init__(self) -> None:
        self._session = Session()

    def get_all_contact(self):
        self.contacts = self._session.query(Contact).all()
        self.contact_list = []  # List of Dictionaries
        for person in self.contacts:
            self.contact_dict = {'contact_id': person.contact_id, 'contact_name': person.contact_name, 'email_id' : person.email_id, 'whatsapp_no': person.whatsapp_no }
            self.contact_list.append(self.contact_dict)
            # print(self.contact_dict)
        return self.contact_list

    def get_all_contact_dataframe(self):
        self.contact_list_of_dictionary = self.get_all_contact()
        self.df_contact = pd.DataFrame()
        self.df_contact = self.df_contact.append(self.contact_list_of_dictionary, ignore_index=True, sort=False)
        return self.df_contact

    def get_all_contact_category(self):
        self.contacts_categories = self._session.query(ContactCategory).all()
        self.contact_category_list = []
        for contact_category in self.contacts_categories:
            self.contact_category_dict = {'contact_category_id': contact_category.contact_category_id, 'contact_id': contact_category.contact_id, 'category': contact_category.category, 'sub_category': contact_category.sub_category , 'priority': contact_category.priority}
            self.contact_category_list.append(self.contact_category_dict)
        return self.contact_category_list

    def get_all_contact_category_dataframe(self):
        self.contact_category_list_of_dictionary = self.get_all_contact_category()
        self.df_contact_category = pd.DataFrame()
        self.df_contact_category = self.df_contact_category.append(self.contact_category_list_of_dictionary, ignore_index=True, sort=False)
        return self.df_contact_category

    def get_all_contact_info_with_category_priority_dataframe(self):
        self.df_contact = self.get_all_contact_dataframe()
        self.df_contact_category = self.get_all_contact_category_dataframe()
        # join contact and category on the basis of contact_id and get the complete information
        self.df_contact_info_with_category = pd.merge(self.df_contact, self.df_contact_category, on='contact_id')
        return self.df_contact_info_with_category


    # def get_specific_contact(self):
    #     pass

    # def get_specific_contact_dataframe(self):
    #     self.specific_contact_list_of_dictionary = self.get_specific_contact()
    #     self.df_specific_contact = pd.DataFrame()
    #     self.df_specific_contact = self.df_specific_contact.append(
    #         self.specific_contact_list_of_dictionary, ignore_index=True, sort=False)
    #     return self.df_specific_contact

    # def get_specific_contact_category(self):
    #     pass

    # def get_specific_contact_category_dataframe(self):
    #     self.specific_contact_category_list_of_dictionary = self.get_specific_contact_category()
    #     self.df_specific_contact_category = pd.DataFrame()
    #     self.df_specific_contact_category = self.df_specific_contact_category.append(self.specific_contact_category_list_of_dictionary, ignore_index=True, sort=False)
    #     return self.df_specific_contact_category

    # def get_specific_contact_info_with_category_priority_dataframe(self):
    #     self.df_specific_contact = self.get_specific_contact_dataframe()
    #     self.df_specific_contact_category = self.get_specific_contact_category_dataframe()
    #     # join contact and category on the basis of contact_id and get the complete information
    #     self.df_specific_contact_info_with_category = pd.merge(self.df_specific_contact, self.df_specific_contact_category, on='contact_id')
    #     return self.df_specific_contact_info_with_category

if __name__ == '__main__':
    objContactExtraction = ContactExtraction()
    df_contact_with_catrgory = objContactExtraction.get_all_contact_info_with_category_priority_dataframe()
    print(df_contact_with_catrgory)
    # objContactExtraction.get_specific_contact_info_with_category_priority_dataframe()


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


