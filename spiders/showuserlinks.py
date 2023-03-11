import scrapy
import pickle 

class ShowuserlinksSpider(scrapy.Spider):
    name = "showuserlinks"

    def __init__(self):
        super(ShowuserlinksSpider, self).__init__()

        f = open(r'C:\Users\hp\OneDrive\Desktop\Projects\place-recommendation\travel_recommender\SITES.pkl', 'rb')
        self.urls = pickle.load(f)
        f.close()

        self.start_urls = [url for url in self.urls if "ShowUserReview" in url]

    def parse(self, response):
        yield {
            'url': f"https://www.tripadvisor.in{response.css('div.see-all-reviews a.ui_button.secondary::attr(href)').get()}" 
        }
