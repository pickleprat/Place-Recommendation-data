import scrapy
import pickle 

class ReviewsSpider(scrapy.Spider):
    name = "reviews"

    def __init__(self):
        super(ReviewsSpider, self).__init__() 
        f = open(r'C:\Users\hp\OneDrive\Desktop\Projects\place-recommendation\travel_recommender\SITES.pkl', 'rb')
        self.urls = pickle.load(f)

        self.start_urls = [
            url for url in self.urls if 'Attraction_Review' in url
        ]
        f.close()
        
    def parse(self, response):

        yield {
            'place': response.css('h1.biGQs._P.fiohW.eIegw::text').get() if response.css('h1.biGQs._P.fiohW.eIegw::text').get() is not None else response.css('h1.QdLfr.b.d.Pn::text').get(), 
            'reviews': response.css('div._c span.yCeTE::text').extract() if response.css('div._c span.yCeTE::text').extract() is not None else response.css('q.QewHA.H4._a span::text').extract(), 
            'rating': response.css('div.biGQs._P.fiohW.hzzSG.uuBRH::text').get() if response.css('div.biGQs._P.fiohW.hzzSG.uuBRH::text') is not None else response.css('div.grdwI.P span.uwJeR.P::text').get(),
        }

