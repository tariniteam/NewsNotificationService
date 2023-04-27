# NewsNotificationService

## **Problem Statement**




## **Solution**





## **Architecture Diagram**




## **Parser**





## **Lexical Analysis/Tokenization**


## **Usage of Query Metadata Parser**



## **Prerequisites**


### Tools/Technologies used




### Required Python packages


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
 
 ![alt text](https://github.com/tariniteam/QueryMetaDataParser/blob/main/Project%20Documentation/Implementation%20Screenshots/2.%20DropdownList%20Table.jpg)
 
 
 ![alt text](https://github.com/tariniteam/QueryMetaDataParser/blob/main/Project%20Documentation/Implementation%20Screenshots/3.%20user%20table.jpg)


### III.	Create Web Pages








 

### IV.	Connect Web Pages using the Flask Framework


•	Connect to sqlite database.

•	Create routing methods to route/redirect web pages based on the GET/POST.

### V.	Create sql_parser python script

•	Create the sql parser python script which will parse the sql query provided by the user and send the metadata extract back to the webapp.

### **Conclusion**



## **GitHub link**



## **Contributors**

1.	Harsha Navalkar ( https://www.linkedin.com/in/harsha-navalkar-00085515b/ )
2.	Vikram Mahapatra (https://www.linkedin.com/in/vikrammahapatra  )

