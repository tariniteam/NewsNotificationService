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

### Errors Faced 

453 - You currently have Essential access which includes access to Twitter API v2 endpoints only. If you need access to this endpoint, you’ll need to apply for Elevated access via the Developer Portal. You can learn more here: https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-leve


### Creation of Twitter Account 

1) Create Twitter Developer Account
Twitter Dev User Name: @TariniTeam

Steps To Get Authentication Keys:
1) Create a Twitter account if you don't already have one
2) Visit 'https://apps.twitter.com' and follow the required prompts to create a developer project (Twitter requires you to    answer some questions before they will approve your account. Approval was nearly instant in my case.)
3) Requesting the API key and secret via the Developer Portal causes Twitter to produce the following three things:
   API key (this is your 'consumer key')
   API secret key (this is your 'consumer secret')
   Bearer token
4) Next, visit the 'Authentication Tokens' area of the Developer Portal and generate an 'Access token & secret'. This will    provide you with the following two items:
   Access token (this is your 'token key')
   Access token secret (this is your 'token secret')

5) The consumer key, consumer secret, token key, and token secret should be sufficient to do Twitter API calls (they were    for me).





## **Architecture Diagram**



## **Usage of NNS**




## **Prerequisites**


### Tools/Technologies used


1.	Python (Download from https://www.python.org/downloads/)
2.	Pycharm
3.	SQLite Database


### Required Python packages

1.	BeautifulSoup
2.	Sqlite3
3.	requests
4. pandas
5. pywhatkit


### Project Structure

## **Initial Setup**

### **Package Installation**

Add python interpreter 
Settings -> Python interpreter -> add local interpreter -> virtualenv environment -> Choose Existing Environment and install the packages 

Install Pywhatkit 
![image](https://user-images.githubusercontent.com/40171616/235209586-cebf6278-e305-446a-839b-9ff5c2ef4d7c.png)



### **Gmail SMTP Connection**
Temporary token 
Smtplib 
Step 1 -  google port = 587(standard secure smtp port)
Step 2  - google SMTP server (smtp.gmail.com)
Step 3 – Temporary token password fr gmail id  from Google Security 
Google account -> security -> app setting -> complete 2 step verification -> “app passwords” section -> enter your gmail password -> Select app (SMTPEMail app) , ->Generate password tokem for the app -> it is one time creation and hence copy and keep it for your application and it is functional for 1 application->  app password will be  created & use this token password along with the gmail id  in the python script to connect it to the SMTP gmail sevrer 
e.g. teamtarini@gmail.com


## **Technical Implementation**


### I.	Prepare your Environment


1.	Create a virtual environment in python 

              virtualenv venv_sql_parser


2.	Install the python packages in the virtual environment described in the pre-requisite section.

              flask
              sql-parser
              sqlite3

To install packages pip install package_name or you can create a new file requirements.txt (this file will contains one package name each row) and install all packages once using : pip install -r requirements.txt
 
 
3.	Create project structure as mentioned in the pre-requisite section.


### II.	Create Database


1.	Create Sqlite Database – QMP_DB.db

 
2.	Create Tables dropdownlist and users in the database QMP_DB.db
 

### III.	Create Web Pages


 
 


### IV.	Connect Web Pages using the Flask Framework



### V.	Create sql_parser python script



### **Conclusion**



## **GitHub link**

•	https://github.com/tariniteam/NewsNotificationService/

## **Contributors**

1.	Harsha Navalkar ( https://www.linkedin.com/in/harsha-navalkar-00085515b/ )
2.	Vikram Mahapatra (https://www.linkedin.com/in/vikrammahapatra  )

