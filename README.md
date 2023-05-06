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


1.	Create Sqlite Database – Person.db

 

 

### III.	Create Framework for News API

 
BeautifulSoup python package is used to for web crawling and data scraping.
TOIApi reads the data from the Times of India website and extracts the required data such as categories, sub category, header title etc.

The class TOIApi does the following functionalities:
 
| Step | Method   | Description    |
| :---:   | :---: | :---: |
| 1. | yield_headline()   | Read individual article links from tag from the Times of India Website and Generate the first top N headline from TOI and pass it to calling generator method   |
| 2. | get_refined_headline_info()   | Extract the data category, sub category, headline, headlineurl for each of the article links.   |
| 3. | get_headline()   | Get the output from method get_refined_headline_info() and convert it into the list of dictionaries.   |
| 4. | get_headline_dataframe()   | Convert the list of dictionaries (of step 3) into dataframe.   |


### IV.	Create Framework for Gmail API

Step 1 -  Standard Secure SMTP Port to be set to 587

Step 2 - Google SMTP server to be set to smtp.gmail.com

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

