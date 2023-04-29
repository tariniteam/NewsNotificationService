from typing import Any


from database_api.sql_queries import ContactExtraction

class NewsNotification:
    def __init__(self) -> None:
        self._objContactExtraction = ContactExtraction()
        self._df_contact_with_catrgory = self._objContactExtraction.get_all_contact_info_with_category_priority_dataframe()
        
    
    def get_contact_detail(df_for_each_contact):
        pass
    
    def process_contact_group(self):
        contact_id_list = self._df_contact_with_catrgory['contact_id'].tolist()
        contact_id_distinct_list = [*set(contact_id_list)]
        for contact in contact_id_distinct_list:
            df_for_each_contact = self._df_contact_with_catrgory.loc[self._df_contact_with_catrgory['contact_id'] == int(contact)]
            contact_name, emil_id, whatsapp_no = self.get_contact_detail(df_for_each_contact)
            self.match_news(contact, df_for_each_contact)