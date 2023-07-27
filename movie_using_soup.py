import requests
import pandas as pd
from bs4 import BeautifulSoup
review=[]
review1=[]
for i in range(1,6):
  url=f'https://www.rottentomatoes.com/browse/movies_in_theaters/?page={i}'
  response=requests.get(url)
  response=response.content
  soup=BeautifulSoup(response,'html.parser')
  div=soup.find('div',class_='discovery-tiles')
  divs=div.find_all('div',class_='js-tile-link')
  al=div.find_all('a',class_="js-tile-link")
  for divi in divs:
    image=divi.find('img')
    title=image.attrs['alt']
    released=divi.find('span',class_='smaller').text
    released=released[19:32].strip()
    c_rating=divi.find('a')
    c_ratings=c_rating.find('score-pairs')
    c_ratingss=c_ratings.attrs['criticsscore']
    p_rating=c_ratings.attrs['audiencescore']
    review.append([title,released,c_ratingss,p_rating])
  for divi in al:
    image=divi.find('img')
    title=image.attrs['alt']
    released=divi.find('span',class_='smaller').text
    released=released[19:32].strip()
    c_rating=divi.find('div')
    c_ratings=c_rating.find('score-pairs')
    c_ratingss=c_ratings.attrs['criticsscore']
    p_rating=c_ratings.attrs['audiencescore']
    review1.append([title,released,c_ratingss,p_rating])
review.extend(review1)
df=pd.DataFrame(review,columns=['title','release','critic_score','human_score'])
df.to_csv('review.csv')