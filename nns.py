
import sys
sys.path.append('../NEWSNOTIFATIONSERVIE')
from database_api.sql_queries import ContactExtraction
from toi_api.toi_api_call import TOIApi
import os


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
    
    def get_associated_news(category, sub_cateogry):
        # get the information in list
        pass

    def match_news(contact_name, email_id, whatsapp_no, df_for_each_contact):
        for index, row in df_for_each_contact.iterrows():
            category = row['category']
            sub_category = row['sub_category']


    def process_contact_group(self):
        contact_id_list = self._df_contact_with_catrgory['contact_id'].tolist()
        contact_id_distinct_list = [*set(contact_id_list)]
        print(contact_id_distinct_list)
        quit()
        for contact in contact_id_distinct_list:
            df_for_each_contact = self._df_contact_with_catrgory.loc[self._df_contact_with_catrgory['contact_id'] == int(contact)]
            contact_name, email_id, whatsapp_no = self.get_contact_detail(df_for_each_contact)
            self.match_news(contact_name, email_id, whatsapp_no, df_for_each_contact)

if __name__ == '__main__':
    print(os.getcwd())
    # ObjNewsNotification = NewsNotification()
    # ObjNewsNotification.process_contact_group()
            

            