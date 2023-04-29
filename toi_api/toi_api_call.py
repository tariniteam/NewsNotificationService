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
        self._number_of_headline = 10

    def yield_headline(self):
        """
        Generate the first top N headline from TOI and pass it to calling generator method
        """
        counter = 0
        for divtag in self._soup.find_all('div', {'class': 'headlines-list'}):
            for ultag in divtag.find_all('ul', {'class': 'clearfix'}):
                if (counter <= 10):
                    for litag in ultag.find_all('li'):
                        counter = counter + 1
                        # print(str(counter) + " - https://timesofindia.indiatimes.com" + litag.find('a')['href'])
                        raw_headline = str(counter) + " - https://timesofindia.indiatimes.com" + litag.find('a')['href']
                        # print(raw_headline)
                        yield raw_headline


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
        headline_list = []  #List of Dictionaries
        for headline in self.yield_headline():            
            print(headline)
            self.category, self.sub_category, self.headline, self.headline_url = self.get_refined_headline_info(headline)
            self.headline_dict = {'category': self.category, 'sub_category': self.sub_category, 'headline': self.headline, 'headline_url': self.headline_url}
            self.headline_list.append(self.headline_dict)

    def get_refined_headline_info(self, headline):
        return self.category, self.sub_category, self.headline, self.headline_url

    def get_headline_dataframe(self):
        """
        """
        self.headline_dict = self.get_headline()
        self.df_headline = pd.DataFrame(headline_dict)
        return df_headline
    
if __name__ == '__main__':
    ObjTOIApi = TOIApi()
    print('test')
    ObjTOIApi.get_headline()

