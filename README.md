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


1.	Python
2.	SQLite Database
3.	Jinja Framework
4.	Bootstrap Framework
5.	HTML, CSS


### Required Python packages

1.	Flask
2.	Sqlite3
3.	Sqlparse 


### Project Structure



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

