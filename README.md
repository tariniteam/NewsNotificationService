# NewsNotificationService
## **Problem Statement**



## **Solution**

1) Web Crawling --- We will scrap all the news content (under various category) -- twitter feed/news scraping (Request/BeautifulSoup/NLTK)

2) Reference Contact with News Choice Category -- 

DB --> ORM (SQL Alchemy | sqllite)
Contacts 
Key|Contacts | Email Id | WhatsApp | Catogory 

CategoryChoice
Contacts Key | Category | Sub Category Choice | Priority 
1 | Sports | Cricket | 2
1 | Sports | Baseball | 1
1 | Sports | TT | 3
1 | Sports | Badminton | 4


3) Retrive contact --> Email and Whatsapp 
4) Connecting to Email and Whatsapp Server 
5) Sending the Information 
6) Storing the information send for only 2 days 



## **Architecture Diagram**



## **Usage of NNS**




## **Prerequisites**


### Tools/Technologies used


1.	Python (Download from https://www.python.org/downloads/)
2.	Pycharm
3.	SQLite Database


### Required Python packages

1.	BeautifulSoup (bs4)
2.	smtplib
3.	Sqlite3
4.	requests
5. pandas
6. pywhatkit


### Project Structure



## **Technical Implementation**


### I.	Prepare your Environment

1.	Create a virtual environment in python 

              virtualenv venv_project_name


2.	Add Python Interpreter to the pycharm project by following below steps:
     - Go to Settings
     - Choose Python Interpreter
     - Add Local Interpreter
     - Choose virtualenv environment
     - Choose Existing Environment and install the packages 


3.	Install the python packages in the virtual environment described in the pre-requisite section.

              pip install <packagename>
       

To install packages pip install package_name or you can create a new file requirements.txt (this file will contains one package name each row) and install all packages once using : pip install -r requirements.txt
 
 
4.	Create project structure as mentioned in the pre-requisite section.


5.  Configure Gmail SMTP Connection

 Generate Temporary token password for gmail id from Google Security 
   - Go to Google Account
   - Go to the Security Section and choose App Setting under the Security Section
   - Complete the two step verification
   - Go the "app passwords" section
   - Enter your gmail password
   - Choose app and provide a name (SMTPEMail app)
   - Generate password token for the app SMTPEMail (It is one time creation and hence copy and keep it for your application and it is functional for 1 application)
   - App password will be  created & use this token password along with the gmail id  in the python script to connect it to the SMTP gmail sevrer 

 
e.g. GmailID: teamtarini@gmail.com, Token:   XXXXXXXXXXXXXXXX



### II.	Create Framework for Database API

Packages Used - sqlalchemy 
Concept used - ORM (Object Relational Mapping) 

1.	Create Sqlite Database – Person.db

#### base.py
- Create an engine to connect to the SQLite Database "Person.db"
- Create a session using the Sessionmaker for the db engine.
- Declare "Base" as a declarative base.


#### db_insert.py
- Generate Database Schema
- create a new session using Session()
- Create test data by creating a contact object (example: contact_1) and by passing the test data into the "Contact" class. (example: contact_1 = Contact(1,'TestName','testemail@gmail.com','+919000000000'))
- Add the contact created to the session.
- Add the user preference of news using the contact category class. (for example:  contact_category_1 = ContactCategory(1,'1','city','lucknow','1')). UserId 1 first preference is to get news associated with the Lucknow city.
- Capture 4 preferences of each user in the above manner and assign it a priority 
- Add the contact_category_1 to the session.
- Commit the Session and then close the session.


#### sql_queries.py

- Create a class "ContactExtraction" in sql_queries.py
- The class "ContactExtraction" has the below listed methods:

| Step | Method   | Description    |
| :---:   | :---: | :---: |
| 1. | get_all_contact()   | Create a List of dictionaries and each dictionary will have the users details such as contact_id,contact_name, email_id,whatsapp_no |
| 2. | get_all_contact_dataframe()   | Convert the contact list of dictionary generated in step 1 to a dataframe  |
| 3. | get_all_contact_category()   |  Create a List of dictionaries and each dictionary will have the users preference such as contact_category_id, contact_category, contact_id, category, sub_category, priority |
| 4. | get_all_contact_category_dataframe()   |  Convert the contact category list of dictionary generated in step 3 to a dataframe   |
| 5. | get_all_contact_info_with_category_priority_dataframe()   | Join contact and category on the basis of contact_id and get the complete information and store it into a dataframe |
 

### III.	Create Framework for News API

 
BeautifulSoup python package is used to for web crawling and data scraping.
TOIApi reads the data from the Times of India website and extracts the required data such as categories, sub category, header title etc.

The class TOIApi does the following functionalities:
 | Step | Method   | Description    |
| :---:   | :---: | :---: |
| 1. | get_all_contact()   | Read individual article links from tag from the Times of India Website and Generate the first top N headline from TOI and pass it to calling generator method   |
| 2. | get_refined_headline_info()   | Extract the data category, sub category, headline, headlineurl for each of the article links.   |
| 3. | get_headline()   | Get the output from method get_refined_headline_info() and convert it into the list of dictionaries.   |
| 4. | get_headline_dataframe()   | Convert the list of dictionaries (of step 3) into dataframe.   |



### IV.	Create Framework for Gmail API

Step 1 - Configure "Configure Gmail SMTP Connection" mentioned in above steps

Step 2 - Install Packages import smtplib, ssl

Step 3 - GMAIL API Class
   - Declare the SMTP port, server, email from and to variables and set  Standard Secure SMTP Port to be set to 587, Google SMTP server to be set to smtp.gmail.com
   - Get the email subject and body in the form of a message from the TOI API Class.
   - Login to the SMTP server using the email_from email id and password credentials
   - Use the sendmail method to send the message to the email_to email IDs.
   - Close the port
   
### V.	Create Framework for Whatsapp API

go to https://developers.facebook.com/?no_redirect=1
Choose Whatsapp Business Platform
Register as a Meta Developer - https://developers.facebook.com/async/registration
sign in to Facebook Account 

Create a Meta App: Go to developers.facebook.com > My Apps > Create App. Select the Business type and follow the prompts on your screen. If you are asked to choose a Use Case as part of the app creation flow, choose Other as your use case, then select Business.


Select apptype as "Business"
AppName = NewsNotificationService

### **Conclusion**



## **GitHub link**

•	https://github.com/tariniteam/NewsNotificationService/

## **Contributors**

1.	Harsha Navalkar ( https://www.linkedin.com/in/harsha-navalkar-00085515b/ )
2.	Vikram Mahapatra (https://www.linkedin.com/in/vikrammahapatra  )

