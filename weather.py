import requests
from bs4 import BeautifulSoup
import pandas as pd
#connect
connect=requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.W0IZOHWFPqM")
html=BeautifulSoup(connect.content,"html.parser")
#desired tag
desireddiv_tag=html.find('div' , id='seven-day-forecast')

#periode name
periode_tags=desireddiv_tag.select(".tombstone-container .period-name")
period=[i.get_text() for i in periode_tags]

#short desc.
short_tags=desireddiv_tag.select(".tombstone-container .short-desc")
short=[i.get_text() for i in short_tags]

#temp.
temp_tags=desireddiv_tag.select(".tombstone-container .temp")
temp=[i.get_text() for i in temp_tags]

#desc
desc_tags=desireddiv_tag.select(".tombstone-container img")
desc=[i["title"] for i in desc_tags]


#coverting into tabular form

table=pd.DataFrame({
	"Description":desc,
	"temperature":temp,
	"short-description":short,
	"period":period
	})
print(table)