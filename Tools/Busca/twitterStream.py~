#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2012 Gustav Arngården

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
import time
import pycurl
import urllib
import json
import oauth2 as oauth
import sys

tweeterCopa = '/media/silvio/Dados/Fatec/6_semestre/TG/dados/dadosTwitter/arq_TwitterCopa.txt'
tweeterFatec = '/media/silvio/Dados/Fatec/6_semestre/TG/dados/dadosTwitter/arq_TwitterFatec.txt'
tweeterDilma = '/media/silvio/Dados/Fatec/6_semestre/TG/dados/dadosTwitter/arq_TwitterDilma.txt'
tweeterPalmeiras = '/media/silvio/Dados/Fatec/6_semestre/TG/dados/dadosTwitter/arq_TwitterPalmeiras.txt'

API_ENDPOINT_URL = 'https://stream.twitter.com/1.1/statuses/filter.json'
USER_AGENT = 'TwitterStream 1.0' # This can be anything really

# You need to replace these with your own values
OAUTH_KEYS = {'consumer_key': "4WwCpBaiTXbB8vdBvtfw",  #GWxtrFDhRwj6jqrXZsWWCQ
              'consumer_secret': "hYKE3CNekT2Rf7XJkgvTJhCVhzsezHmgBNyIDL6bQ", #s85MMFdRfJSHpYyRZAl1kzVNkZ4XslkIZHDvO3ujw
              'access_token_key': "1393287416-W3JwLoj8m055Ha7vposdh4Qskz3dN80IEKikwfu", #1393287416-g1E6YCH9fqbQDdEXaBCeWKufil3A1ZiZeMvMvhe
              'access_token_secret': "Diewxe13VSQRZZy5qa3th4ugMNRvR3SvI1sa8pd8afkcy"} # X7ZsdsdtfXIe7DAO6l3vJYHLDa5cKlVjwFbhSuqfMc

count=0
n=500
var = sys.argv[1]
# These values are posted when setting up the connection
POST_PARAMS = {'include_entities': 0,
               'stall_warning': 'true',
               'track': var}

class TwitterStream:
    def __init__(self, timeout=False):
        self.oauth_token = oauth.Token(key=OAUTH_KEYS['access_token_key'], secret=OAUTH_KEYS['access_token_secret'])
        self.oauth_consumer = oauth.Consumer(key=OAUTH_KEYS['consumer_key'], secret=OAUTH_KEYS['consumer_secret'])
        self.conn = None
        self.buffer = ''
        self.timeout = timeout
        self.setup_connection()

    def setup_connection(self):
        """ Create persistant HTTP connection to Streaming API endpoint using cURL.
        """
        if self.conn:
            self.conn.close()
            self.buffer = ''
        self.conn = pycurl.Curl()
        # Restart connection if less than 1 byte/s is received during "timeout" seconds
        if isinstance(self.timeout, int):
            self.conn.setopt(pycurl.LOW_SPEED_LIMIT, 1)
            self.conn.setopt(pycurl.LOW_SPEED_TIME, self.timeout)
        self.conn.setopt(pycurl.URL, API_ENDPOINT_URL)
        self.conn.setopt(pycurl.USERAGENT, USER_AGENT)
        # Using gzip is optional but saves us bandwidth.
        self.conn.setopt(pycurl.ENCODING, 'deflate, gzip')
        self.conn.setopt(pycurl.POST, 1)
        self.conn.setopt(pycurl.POSTFIELDS, urllib.urlencode(POST_PARAMS))
        self.conn.setopt(pycurl.HTTPHEADER, ['Host: stream.twitter.com',
                                             'Authorization: %s' % self.get_oauth_header()])
        # self.handle_tweet is the method that are called when new tweets arrive
        self.conn.setopt(pycurl.WRITEFUNCTION, self.handle_tweet)

    def get_oauth_header(self):
        """ Create and return OAuth header.
        """
        params = {'oauth_version': '1.0',
                  'oauth_nonce': oauth.generate_nonce(),
                  'oauth_timestamp': int(time.time())}
        req = oauth.Request(method='POST', parameters=params, url='%s?%s' % (API_ENDPOINT_URL,
                                                                             urllib.urlencode(POST_PARAMS)))
        req.sign_request(oauth.SignatureMethod_HMAC_SHA1(), self.oauth_consumer, self.oauth_token)
        return req.to_header()['Authorization'].encode('utf-8')

    def start(self):
        """ Start listening to Streaming endpoint.
        Handle exceptions according to Twitter's recommendations.
        """
        backoff_network_error = 0.25
        backoff_http_error = 5
        backoff_rate_limit = 60
        while True:
            self.setup_connection()
            try:
                self.conn.perform()
            except:
                # Network error, use linear back off up to 16 seconds
                print ('Network error: %s' % self.conn.errstr())
                print ('Waiting %s seconds before trying again' % backoff_network_error)
                time.sleep(backoff_network_error)
                backoff_network_error = min(backoff_network_error + 1, 16)
                continue
            # HTTP Error
            sc = self.conn.getinfo(pycurl.HTTP_CODE)
            if sc == 420:
                # Rate limit, use exponential back off starting with 1 minute and double each attempt
                print ('Rate limit, waiting %s seconds' % backoff_rate_limit)
                time.sleep(backoff_rate_limit)
                backoff_rate_limit *= 2
            else:
                # HTTP error, use exponential back off up to 320 seconds
                print ('HTTP error %s, %s' % (sc, self.conn.errstr()))
                print ('Waiting %s seconds' % backoff_http_error)
                time.sleep(backoff_http_error)
                backoff_http_error = min(backoff_http_error * 2, 320)

    def handle_tweet(self, data):
        """ This method is called when data is received through Streaming endpoint.
        """
        self.buffer += data
        arqfile='vazio'
        global count,n
        if data.endswith('\r\n') and self.buffer.strip():
            # complete message received
            message = json.loads(self.buffer)
            self.buffer = ''
            msg = ''
            if message.get('limit'):
                print ('Rate limiting caused us to miss %s tweets' % (message['limit'].get('track')))
            elif message.get('disconnect'):
                raise Exception('Got disconnect: %s' % message['disconnect'].get('reason'))
            elif message.get('warning'):
                print ('Got warning: %s' % message['warning'].get('message'))
            else:
                #print ('Got tweet with text: %s\n' % message.get('text'))
                if (var == 'dilma'):
                    arqfile = tweeterDilma          
                    f = open(arqfile , 'a')
                    print ("Salvo: %s "%message.get('text'))
                    f.write(str(message.get('text').encode('utf-8')) +'\n\n')
                    f.close()
                    count=count+1
                    print ("Count: %d "%count)
                elif (var == 'Fatec'):
                    arqfile = tweeterFatec          
                    f = open(arqfile , 'a')
                    print ("Salvo: %s "%message.get('text'))
                    f.write(str(message.get('text').encode('utf-8')) +'\n\n')
                    f.close()
                    count=count+1
                    print ("Count: %d "%count)
                elif (var == 'palmeiras'):
                    arqfile = tweeterPalmeiras
                    f = open(arqfile , 'a')
                    print ("Salvo: %s "%message.get('text'))
                    f.write(str(message.get('text').encode('utf-8')) +'\n\n')
                    f.close()
                    count=count+1
                    print ("Count: %d "%count)
                elif (var == 'copa'):
                    arqfile = tweeterCopa          
                    f = open(arqfile , 'a')
                    if ( 'Brasil' in message.get('text') or '2014' in message.get('text') and ('lograr') not in message.get('text') and ('ayer') not in message.get('text')):
                        print ("Salvo: %s "%message.get('text'))
                        f.write(str(message.get('text').encode('utf-8')) +'\n\n')
                        f.close()
                        count=count+1
                        print ("Count: %d "%count)
                 
                if (count == n):
                    sys.exit()
                 
                

if __name__ == '__main__':
    ts = TwitterStream()
    ts.setup_connection()
    ts.start()
