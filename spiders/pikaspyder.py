import scrapy
import pickle 

class PikaspyderSpider(scrapy.Spider):
    name = "pikaspyder"

    def __init__(self):
        super(PikaspyderSpider, self).__init__()

        f = open(r'C:\Users\hp\OneDrive\Desktop\Projects\place-recommendation\travel_recommender\user_reviews.pkl', 'rb')
        self.start_urls = pickle.load(f)
        f.close()


    def parse(self, response):
        yield {
            'place': response.css('h1.biGQs._P.fiohW.eIegw::text').get(), 
            'review': response.css('div.biGQs._P.pZUbB.KxBGd span.yCeTE::text').extract(),
            'rating': response.css('div.biGQs._P.fiohW.hzzSG.uuBRH::text').get()
        }
