
from tweepy import OAuthHandler
import tweepy as tw
import pandas as pd
from pandas import ExcelWriter
const axios = require("axios");

const options = {
  method: 'GET',
  url: 'https://twitter135.p.rapidapi.com/AutoComplete/',
  params: {q: 'Elon'},
  headers: {
    'X-RapidAPI-Host': 'twitter135.p.rapidapi.com',
    'X-RapidAPI-Key': 'f852dec623mshc6fa9025feb58afp16025ejsn3aa2be7aa1d7'
  }
};

axios.request(options).then(function (response) {
	console.log(response.data);
}).catch(function (error) {
	console.error(error);
});

tweets = []

count = 1

"""Twitter will automatically sample the last 7 days of data. Depending on how many total tweets there are with the specific hashtag, keyword, handle, or key phrase that you are looking for, you can set the date back further by adding since= as one of the parameters. You can also manually add in the number of tweets you want to get back in the items() section."""

for tweet in tw.Cursor(api.search_tweets, q="@NarendraModi", count=10).items(10):
    count += 1
    try: 
        data = [ tweet.created_at, tweet.id, tweet.text, tweet.user._json['screen_name'], tweet.user._json['name'],  tweet.user._json['created_at'],tweet.entities['urls']]
        data = tuple(data)
        tweets.append(data)

    except tw.TweepError as e:
        print(e.reason)
        continue

    except StopIteration:
        break

df = pd.DataFrame(tweets, columns = ['created_at','tweet_id', 'tweet_text', 'screen_name', 'name','account_creation_date','urls'])

"""Add the path to the folder you want to save the CSV file in as well as what you want the CSV file to be named inside the single quotations"""
df.to_csv(path_or_buf = 'Tweets.csv', index=True)
print("tweets are added to csv file")