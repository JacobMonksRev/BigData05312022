import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
import socket
import json

consumer_key = 'gdhsiOBUsfhnQuLVVvTuUIEJJ'
consumer_secret = 'z3j5OlkZEQEdPWvKZaMYSygLXaWCKa7UsM9S5ueBToo8s9wGpq'
access_token = '1549240454767644674-DJYEF4kGjSAcEZMxivDZ2WD1uQ40d5'
access_secret = 'qfYRYeLsvrxTCxFDupWWsX0Pbid6piAReiY8b2RB8D7no'

class TweetsListener(Stream):
    def __init__(self, csocket):
        self.client_socket = csocket
    def on_data(self, data):
        try:
            msg = json.loads(data)
            print(msg['text']).encode('utf-8')
            self.client_socket.send(msg['text'].encode('utf-8'))
        except BaseException as e:
            print("Error on data: " + str(e))
    def on_error(self, status):
        print(status)

def sendData(c_socket):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    twitter_stream = Stream(auth.consumer_key, auth.consumer_secret, access_token, access_secret, TweetsListener(c_socket))
    twitter_stream.filter(track=['football'])

if __name__ == "__main__":
  s = socket.socket()         # Create a socket object
  host = "127.0.0.1"     # Get local machine name
  port = 5555                 # Reserve a port for your service.
  s.bind((host, port))        # Bind to the port

  print("Listening on port: %s" % str(port))

  s.listen(5)                 # Now wait for client connection.
  c, addr = s.accept()        # Establish connection with client.

  print( "Received request from: " + str( addr ) )

  sendData( c )