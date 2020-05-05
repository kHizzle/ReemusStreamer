import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json

consumer_key="c7qa8QDltERcdoo3cq1seJfkP"
consumer_secret="vxW5gjcevx3DJG3BrfPSyjxiN8oIYwZ7R4UT2Oigq2EEhdz4Ea"
access_token = "992807681281978369-yJAPYt0PfqbLi6iIklkb1WjkE2a0guL"
access_secret="777XoE0qsdj5XuFm62apRR8yOP6BtZZu0JMEKHyV09JcR"

class TweetsListener(StreamListener):
  def __init__(self, csocket):
      self.client_socket = csocket
  def on_data(self, data):
      try:
          msg = json.loads( data )
          self.client_socket.send( msg['text'].encode('utf-8') )
          return True
      except BaseException as e:
          print("Error on_data: %s" % str(e))
      return True
  def on_error(self, status):
      print(status)
      return True

def sendData(c_socket):
    print("OAuthHandler")
    auth = OAuthHandler(consumer_key, consumer_secret)
    print("Set Access Token")
    auth.set_access_token(access_token, access_secret)
    print("Stream")
    twitter_stream = Stream(auth, TweetsListener(c_socket))
    print("Filter")
    twitter_stream.filter(track=['labradoodle'])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                             # Create a socket object
host = "0.0.0.0"            # Get local machine name
port = 5555                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
port2 = s.getsockname() 
s.listen(5)                 # Now wait for client connection.tweet_stream.py
print("Waiting for a connection")
c, addr = s.accept()        # Establish connection with client.   
print("Received request from: " + str(addr))
