import tweepy

#rocket = RocketChatAPI(settings={'username': '', 'password': '', 'domain': ''})

consumer_key = "J"
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

keywords = "34713362,1652541,25073877,18856867,42589787,69620713,16815644,3108351,28366310,18949452,59393368,27652717,624413,19399038,36499730"

def from_creator(status):
    if hasattr(status, 'retweeted_status'):
        return False
    elif status.in_reply_to_status_id != None:
        return False
    elif status.in_reply_to_screen_name != None:
        return False
    elif status.in_reply_to_user_id != None:
        return False
    else:
        return True

class MyStreamListener(tweepy.StreamListener):
  def on_status(self, status):
    if from_creator(status):
      try:
        print("("+status.user.name+")"+"----"+status.text)
        #rocket.send_message(status.text, 'twitter')
      except:
        pass

print("Connecting to twitter and pulling stream")
print("")
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(follow=[keywords])

