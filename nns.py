
import sys
# sys.path.append('../NEWSNOTIFATIONSERVIE')
from database_api.sql_queries import ContactExtraction
from toi_api.toi_api_call import TOIApi
import os
from database_api.base import Base
from database_api.model.contact import Contact
from database_api.model.contact_category import ContactCategory    
from database_api.base import Session, engine, Base



class NewsNotification:
    def __init__(self) -> None:
        self._objContactExtraction = ContactExtraction()
        self._df_contact_with_catrgory = self._objContactExtraction.get_all_contact_info_with_category_priority_dataframe()        
        self._df_toi_headline = TOIApi.get_headline_dataframe()

            
    def get_contact_detail(self, df_for_each_contact):
        contact_name = df_for_each_contact['contact_name'].iloc[0]
        email_id = df_for_each_contact['email_id'].iloc[0]
        whatsapp_no = df_for_each_contact['whatsapp_no'].iloc[0]
        return contact_name, email_id, whatsapp_no
    # 
    def get_associated_news(self, contact_name, email_id, whatsapp_no, df_for_each_contact):
        # get the information in list
        each_contact_category_list = df_for_each_contact['category'].tolist()
        each_contact_sub_category_list = df_for_each_contact['sub_category'].tolist()
        user_category_sub_category_dict =  dict(zip(each_contact_category_list,each_contact_sub_category_list))
        # print(user_category_sub_category_dict)
        # print(self._df_toi_headline)
        self._df_toi_headline.to_csv('toi_headline.csv')
        # user_selected_headline_df = self._df_toi_headline[(self._df_toi_headline['category'] == str(k)) & (self._df_toi_headline['sub_category'] == str(v)) ]
        # quit()
        for k, v in user_category_sub_category_dict.items():
            user_selected_headline_df = \
                    self._df_toi_headline[(self._df_toi_headline['category'].str.contains(str(k))) & \
                                          (self._df_toi_headline['sub_category'].str.contains(str(v)) \
                                           | self._df_toi_headline['sub_category'].str.contains('')) ]
            print(f"{str(k)}, {str(v)}")
            # print(user_selected_headline_df)
            
            # quit()
        return each_contact_category_list, each_contact_sub_category_list
        

    def match_news(self, contact_name, email_id, whatsapp_no, df_for_each_contact):
        # each_contact_category_list,each_contact_sub_category_list = \
        self.get_associated_news(contact_name, email_id, whatsapp_no, df_for_each_contact)
        # for index, row in df_for_each_contact.iterrows():
        #     category = row['category']
        #     sub_category = row['sub_category']


    def process_contact_group(self):
        contact_id_list = self._df_contact_with_catrgory['contact_id'].tolist()
        contact_id_distinct_list = [*set(contact_id_list)]
        # print(contact_id_distinct_list)
        # quit()
        for contact in contact_id_distinct_list:
            df_for_each_contact = self._df_contact_with_catrgory.loc[self._df_contact_with_catrgory['contact_id'] == int(contact)]
            contact_name, email_id, whatsapp_no = self.get_contact_detail(df_for_each_contact)
            print(contact_name, email_id, whatsapp_no)
            print(df_for_each_contact)
            self.match_news(contact_name, email_id, whatsapp_no, df_for_each_contact)

if __name__ == '__main__':
    # print(os.getcwd())
    ObjNewsNotification = NewsNotification()
    ObjNewsNotification.process_contact_group()
        

            