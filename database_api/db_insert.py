from datetime import date
from model.contact import Contact
from base import Session, engine, Base
from model.contact_category import ContactCategory


# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

# 4 - create Conact

contact_1 = Contact(1,'Rajesh','viki.keshari@gmail.com','+919820663554')
contact_2 = Contact(2,'Sanjana','navalkar60@gmail.com','+919699683328')
contact_3 = Contact(3,'Richa','viki.keshari@gmail.com','+919820663554')
contact_4 = Contact(4,'Rohit','navalkar60@gmail.com','+919699683328')


session.add(contact_1)
session.add(contact_2)
session.add(contact_3)
session.add(contact_4)

contact_category_1 = ContactCategory(1,'1','city','lucknow','1')
contact_category_2 = ContactCategory(2,'1','india','','2')
contact_category_3 = ContactCategory(3,'1','election','','3')
contact_category_4 = ContactCategory(4,'1','video','news','4')

session.add(contact_category_1)
session.add(contact_category_2)
session.add(contact_category_3)
session.add(contact_category_4)

contact_category_5 = ContactCategory(5,'2','city','bengaluru','1')
contact_category_6 = ContactCategory(6,'2','city','nagpur','2')
contact_category_7 = ContactCategory(8,'2','sports','cricket','3')
contact_category_8 = ContactCategory(7,'2','election','','4')
session.add(contact_category_5)
session.add(contact_category_6)
session.add(contact_category_7)
session.add(contact_category_8)

contact_category_9 = ContactCategory(9,'3','city','gurgaon','1')
contact_category_10 = ContactCategory(10,'3','india','','2')
contact_category_11 = ContactCategory(11,'3','entertainment','tamil','3')
contact_category_12 = ContactCategory(12,'3','video','news','4')
session.add(contact_category_9)
session.add(contact_category_10)
session.add(contact_category_11)
session.add(contact_category_12)

contact_category_13 = ContactCategory(13,'4','city','lucknow','1')
contact_category_14 = ContactCategory(14,'4','india','','2')
contact_category_15 = ContactCategory(15,'4','election','','3')
contact_category_16 = ContactCategory(16,'4','video','news','4')
session.add(contact_category_13)
session.add(contact_category_14)
session.add(contact_category_15)
session.add(contact_category_16)


# 10 - commit and close session
session.commit()
session.close()