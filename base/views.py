from django.shortcuts import render

from django.views.generic import CreateView                             # For SignUp form Page  
from . import forms                                                     # For SignUp form Page 
from django.urls import reverse_lazy                                    # For signUp page methode 2
from django.contrib.auth.decorators import login_required

import re
import snscrape.modules.twitter as sntwitter                            # For scrapping twitter

import pandas as pd




def get_tweets(query, limit):
    tweets = []
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.date, tweet.username, tweet.content, tweet.likeCount, tweet.replyCount, tweet.retweetCount, tweet.url])
    df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet', 'Like', 'Replay', 'Retweet', 'Url'])
    return df


def about(request):
    return render(request, 'about.html')

# Create your views here.
def result(request):
    pass

def home_view(request):


    import random
    myliste = ["SIDA", "HIV", "AIDS"]
    # query = f"{random.choice(myliste)} min_faves:100 lang:fr"
    query = "(#sida) min_faves:1000 lang:fr"
    df = get_tweets(query, int(3))
    df = df.sort_values(['Like', 'Retweet','Replay'],ascending=False)

        ### Get  3 Tweets most liked ###
    if len(df)>=3:
                tweet_1_date = df.iloc[0]['Date']
                tweet_2_date = df.iloc[1]['Date']
                tweet_3_date = df.iloc[2]['Date']

                tweet_1_User = df.iloc[0]['User']
                tweet_2_User = df.iloc[1]['User']
                tweet_3_User = df.iloc[2]['User']


                tweet_1_Tweet = df.iloc[0]['Tweet']
                tweet_2_Tweet = df.iloc[1]['Tweet']
                tweet_3_Tweet = df.iloc[2]['Tweet']  

                tweet_1_Like = df.iloc[0]['Like']
                tweet_2_Like = df.iloc[1]['Like']
                tweet_3_Like = df.iloc[2]['Like']    

                tweet_1_Replay = df.iloc[0]['Replay']
                tweet_2_Replay = df.iloc[1]['Replay']
                tweet_3_Replay = df.iloc[2]['Replay'] 

                tweet_1_Retweet = df.iloc[0]['Retweet']
                tweet_2_Retweet = df.iloc[1]['Retweet']
                tweet_3_Retweet = df.iloc[2]['Retweet']    

                tweet_1_Url = df.iloc[0]['Url']
                tweet_2_Url = df.iloc[1]['Url']
                tweet_3_Url = df.iloc[2]['Url']    

    return render(request, 'home.html', {
                                            'tweet_1_date':tweet_1_date,
                                            'tweet_2_date':tweet_2_date,
                                            'tweet_3_date':tweet_3_date,
                                            "tweet_1_User":tweet_1_User,
                                            "tweet_2_User":tweet_2_User,
                                            "tweet_3_User":tweet_3_User,
                                            "tweet_1_Tweet":tweet_1_Tweet,
                                            "tweet_2_Tweet":tweet_2_Tweet,
                                            "tweet_3_Tweet":tweet_3_Tweet,
                                            "tweet_1_Like":tweet_1_Like,
                                            "tweet_2_Like":tweet_2_Like,
                                            "tweet_3_Like":tweet_3_Like,
                                            "tweet_1_Replay":tweet_1_Replay,
                                            "tweet_2_Replay":tweet_2_Replay,
                                            "tweet_3_Replay":tweet_3_Replay,
                                            "tweet_1_Retweet":tweet_1_Retweet,
                                            "tweet_2_Retweet":tweet_2_Retweet,
                                            "tweet_3_Retweet":tweet_3_Retweet,
                                            "tweet_1_Url" : tweet_1_Url,
                                            "tweet_2_Url" : tweet_2_Url,
                                            "tweet_3_Url" : tweet_3_Url,
    }
    )

#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
###                                                                                                                           ###
###                                                     SignUp form Page                                                      ###
###                                                                                                                           ###
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################

class SignupPage(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = './registration/signup.html'

