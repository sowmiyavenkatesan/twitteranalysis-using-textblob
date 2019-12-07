from twitterscraper import query_tweets
import datetime as dt
import pandas as pd
from textblob import TextBlob
begin=dt.date(2019,4,15)
end=dt.date(2019,4,24)
limit=1000
lang='english'
tweets=query_tweets("Donald Trump",begindate=begin,enddate=end,limit=limit,lang=lang)
df=pd.DataFrame(t.__dict__ for t in tweets)
df=df['text']
for i in df:
    print(i)
    d=print(TextBlob(i).sentiment)

