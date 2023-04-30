
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
    
    def get_associated_news(self, contact_id, category, sub_category, df_for_each_contact):
        each_contact_category_list = df_for_each_contact['category'].tolist()
        each_contact_sub_category_list = df_for_each_contact['sub_category'].tolist()
        return each_contact_category_list, each_contact_sub_category_list

## from email.message import EmailMessage
    def match_news(self, contact_name, email_id, whatsapp_no, df_for_each_contact):
        each_contact_category_list,each_contact_sub_category_list = self.get_associated_news(contact_name, email_id, whatsapp_no, df_for_each_contact)
        for index, row in df_for_each_contact.iterrows():
            category = row['category']
            sub_category = row['sub_category']
            priority = row['priority']

            message = f"""\
                     <html><head></head><body>
                     <p>News Headline for Today</p>
                     <p>Hey {contact_name},  Please have a look at today's important headlines.</p>
                    {build_table(df_headline.loc[:, ['headline', 'headline_url']] )}   </body></html>"""

            if (category in each_contact_category_list) and (sub_category in each_contact_sub_category_list) and (priority<=3):
                      send_email_notification(contact_name, email_id, message)
                      send_whatsapp_notification(contact_name, whatsapp_no, message)

    def send_email_notification (self, contact_name, email_to, message,  email_from="tariniteam@gmail.com"):
        simple_email_context = ssl.create_default_context()

        try:
            # Connect to the server
            print("Connecting to server...")
            TIE_server = smtplib.SMTP(smtp_server, smtp_port)
            TIE_server.starttls(context=simple_email_context)
            TIE_server.login(email_from, pswd)
            print("Connected to server :-)")

            # Send the actual email
            print()
            print(f"Sending email to - {email_to}")
            TIE_server.sendmail(email_from, email_to, message)
            print(f"Email successfully sent to - {email_to}")

        # If there's an error, print it out
        except Exception as e:
            print(e)

        # Close the port
        finally:
            TIE_server.quit()

    def send_whatsapp_notification(self, contact_name, message, whatsapp_no):
        pass


    def process_contact_group(self):
        contact_id_list = self._df_contact_with_catrgory['contact_id'].tolist()
        contact_id_distinct_list = [*set(contact_id_list)]
        print(contact_id_distinct_list)
        for contact in contact_id_distinct_list:
            df_for_each_contact = self._df_contact_with_catrgory.loc[self._df_contact_with_catrgory['contact_id'] == int(contact)]
            contact_name, email_id, whatsapp_no = self.get_contact_detail(df_for_each_contact)
            self.match_news(contact_name, email_id, whatsapp_no, df_for_each_contact)

if __name__ == '__main__':
    print(os.getcwd())
    # ObjNewsNotification = NewsNotification()
    # ObjNewsNotification.process_contact_group()
            

            