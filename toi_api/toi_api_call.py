import requests
from bs4 import BeautifulSoup
import pandas as pd

class TOIApi:
    """
    This Modue is will Call TOI api to extract the headline from today and then depending upon the need of the project, 
    it will cleanse and store the headline in the dictionary then this headline dataframe will be passed to the calling 
    module
    """
    def __init__(self) -> None:
        """
        This will intialize the 
        """
        self._url = "https://timesofindia.indiatimes.com/home/headlines"
        self._page_request = requests.get(self._url)
        self._data = self._page_request.content
        self._soup = BeautifulSoup(self._data,"html.parser")
        self._number_of_headline = 100

    def yield_headline(self):
        """
        Generate the first top N headline from TOI and pass it to calling generator method
        """
        counter = 0
        for divtag in self._soup.find_all('div', {'class': 'headlines-list'}):
            for ultag in divtag.find_all('ul', {'class': 'clearfix'}):                
                for litag in ultag.find_all('li'):
                    if (counter <= self._number_of_headline):
                        counter = counter + 1                       
                        raw_headline = "https://timesofindia.indiatimes.com" + litag.find('a')['href']                        
                        yield raw_headline
                    else:
                        break


    def get_headline(self):
        """
        Get the yield headline and convert it into list of dictionaries.
        Four column dictionary are getting formed with column:
        1) Category
        2) Sub Category
        3) Headline
        4) HeadlineURL
        each yield will form a single dictionary and such N dictionary will form N item in the list.
        """
        self.headline_list = []  #List of Dictionaries
        for headline in self.yield_headline():            
            # print("Headline inside get_headline method", headline)
            self.category, self.sub_category, self.headline, self.headline_url = self.get_refined_headline_info(headline)
            self.headline_dict = {'category': self.category, 'sub_category': self.sub_category, 'headline': self.headline, 'headline_url': self.headline_url}
            self.headline_list.append(self.headline_dict)
            # print("List of Dictionary: ", self.headline_list)
        return self.headline_list

    def get_refined_headline_info(self, headline):
        #print("Get Refined Headline Info", headline)
        Node = "timesofindia.indiatimes.com"
        self.headline_url = headline
        self.headline_split_list = self.headline_url.split("/")
        #print ("List",self.headline_split_list )
        self.headline =self.headline_split_list[-3].replace('-', ' ')
        self.category =self.headline_split_list[self.headline_split_list.index(Node) + 1]
        if len(self.headline_split_list) <= 7:
            self.sub_category = None
        else:
            self.sub_category =self.headline_split_list[self.headline_split_list.index(Node) + 2]

        return self.category, self.sub_category, self.headline, self.headline_url

    @classmethod
    def get_headline_dataframe(class_instance):
        """
        """
        # print("Inside get_headline_dataframe")
        class_instance.headline_list_of_dictionary = class_instance().get_headline()
        # print( "self.headline_dict", class_instance.headline_list_of_dictionary)
        class_instance.df_headline = pd.DataFrame()
        class_instance.df_headline = class_instance.df_headline.append(class_instance.headline_list_of_dictionary, ignore_index=True, sort=False)       
        return class_instance.df_headline
    
if __name__ == '__main__':
    df_headline = TOIApi.get_headline_dataframe()
    print(df_headline)

