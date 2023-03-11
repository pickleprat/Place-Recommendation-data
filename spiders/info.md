# selectors in info.md 

# collecting all review objects 
reviews = response.css('div._c span.yCeTE::text')

# getting all the headers 
header = response.css('h1.biGQs._P.fiohW.eIegw').get()

# Getting rating
review = response.css('div.biGQs._P.fiohW.hzzSG.uuBRH::text').extract()

# Get username 
username = response.css('a.BMQDV._F.G-.wSSLS.SwZTJ.FGwzt.ukgoS::text').extract()

# status
status = response.css('div.RpeCd::text').extract()


# Hotel Review Spyder 

# Hotel Heading 
response.css('h1#HEADING::text').get()

# Hotel rating 
response.css('div.grdwI.P span.uwJeR.P::text').get()

# Hotel review 
 response.css('div.YibKl.MC.R2.Gi.z.Z.BB.pBbQr q.QewHA.H4._a span::text').extract()