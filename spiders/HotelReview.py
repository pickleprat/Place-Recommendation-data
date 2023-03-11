import scrapy
import pickle 

class HotelreviewSpider(scrapy.Spider):
    name = "HotelReview"
    
    def __init__(self):
        super(HotelreviewSpider, self).__init__()

        #Getting all the links with Hotel Review in them. 
        with open(r'C:\Users\hp\OneDrive\Desktop\Projects\place-recommendation\travel_recommender\SITES.pkl', 'rb') as f:
            reviews = pickle.load(f)

        self.start_urls = [
            review for review in reviews if "Hotel_Review" in review
        ]

    def parse(self, response):

        yield {
            'place':response.css('h1#HEADING::text').get(), 
            'reviews':response.css('div.YibKl.MC.R2.Gi.z.Z.BB.pBbQr q.QewHA.H4._a span::text').extract(), 
            'rating':response.css('div.grdwI.P span.uwJeR.P::text').get()
        }
