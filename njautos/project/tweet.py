# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:09:21 2017

@author: zmx
"""
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import datetime
import json, time
# set your keys to access tweets 
consumer_key = 'zUuyMTkXox4DobpKChBt5cJfB'
consumer_secret = 'r5bKzPIhxKLwgfwFB9jgfAYBpmOKVTn6JAHgpTkqj3Gp17qLCx'
access_token = '831333910084726785-R0qh3YCVAz3k8KhcX3ElYd2FfKlVH6s'
access_secret = 'HhPH1pjoA0tWqiWnW6LTU6A9671Xkjeis8fGVW10NnwQr'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

class MyListener(StreamListener):   
    # constructor
    def __init__(self, output_file, time_limit):        
            # attribute to get listener start time
            self.start_time=datetime.datetime.now()
            # attribute to set time limit for listening
            self.time_limit=time_limit            
            # attribute to set the output file
            self.output_file=output_file            
            # initiate superclass's constructor
            StreamListener.__init__(self)    
    # on_data is invoked when a tweet comes in
    # overwrite this method inheritted from superclass
    # when a tweet comes in, the tweet is passed as "data"
    def on_data(self, data):        
        # get running time
        running_time=datetime.datetime.now()-self.start_time
        print(running_time)        
        # check if running time is over time_limit
        if running_time.seconds/60.0<self.time_limit:            
            # ***Exception handling*** 
            # If an error is encountered, 
            # a try block code execution is stopped and transferred
            # down to the except block. 
            # If there is no error, "except" block is ignored
            try:
                # open file in "append" mode
                with open(self.output_file, 'a') as f:
                    # Write tweet string (in JSON format) into a file
                    f.write(data)                    
                    # continue listening
                    return True               
            # if an error is encountered
            # print out the error message and continue listening           
            except BaseException as e:
                print("Error on_data:", str(e))               
                # if return "True", the listener continues
                return True           
        else:  # timeout, return False to stop the listener
            print("time out")
            return False
    # on_error is invoked if there is anything wrong with the listener
    # error status is passed to this method
    def on_error(self, status):
        print(status)
        # continue listening by "return True"
        return True
    
def get_tweets():
    brand_name = "Toyota"
    out_text = brand_name + ".txt"
    out_json = brand_name + ".json"
    tweet_listener=MyListener(output_file=out_text,time_limit=60) # we scrape every brand we need for 60 minutes
    
    # start a staeam instance using authentication and the listener
    twitter_stream = Stream(auth, tweet_listener)
    # filtering tweets by topics
    twitter_stream.filter(track=['#Toyota', '#toyota'])
    time.sleep(0.5)
    
    tweets=[]
    with open(out_text, 'r') as f:
    # each line is one tweet string in JSON format
        for line in f:
            tweet = json.loads(line)               
            tweets.append(tweet)
    # write the whole list back to JSON
    json.dump(tweets, open(out_json,'w'), indent=4) # use indent=4 to make the json file more readable
    
    # to load the whole list
    # pay attention to json.load and json.loads
    tweets=json.load(open(out_json,'r'))
    print("number of tweets:", len(tweets))
    # we use all_tweets to store the result
    all_tweets=[]
    
    for tweet in tweets:
        all_tweets.append(tweet["text"])
    return all_tweets

if __name__ == "__main__":
    content=get_tweets()        
    print content
