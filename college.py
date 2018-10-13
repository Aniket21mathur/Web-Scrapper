import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

#connect like this
connect=requests.get("https://www.topuniversities.com/student-info/choosing-university/worlds-top-100-universities")
html=BeautifulSoup(connect.content,"html.parser")

#get ranks 
ranks_tags=html.find_all('td', style='width: 52px;')
ranks=[rt.get_text() for rt in ranks_tags]

#get names
#no IIT in TOP 100 quite sad!
universities_tags=html.find_all('td', style='width: 455px;')
universities=[uni.get_text() for uni in universities_tags]
#get location
#no INDIA sad af.
locations_tags=html.find_all('td', style='width: 124px;')
locations=[lo.get_text() for lo in locations_tags]

#organising in tabular form
table=pd.DataFrame({
	"A":ranks,
	"B":universities,
	"C":locations
	})
print(table)
