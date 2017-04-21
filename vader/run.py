"""
    Azure Functions HTTP Example Code for Python
    
    Created by Anthony Eden
    http://MediaRealm.com.au/
"""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'lib')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'env/Lib/site-packages')))

import json
from AzureHTTPHelper import HTTPHelper
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# This is a little class used to abstract away some basic HTTP functionality
http = HTTPHelper()
body = ""
if 'text' in http.get:
    text = http.get['text']
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(text)
    body = str(vs)
else:
    body = "You need to add text param like this >>\nhttps://vaderpoc.azurewebsites.net/api/vader?text=this+is+a+sample+text"





# All data to be returned to the client gets put into this dict
returnData = {
    #HTTP Status Code:
    "status": 200,
    
    #Response Body:
    "body": body,
    
    # Send any number of HTTP headers
    "headers": {
        "Content-Type": "text/plain"
    }
}

# Output the response to the client
output = open(os.environ['res'], 'w')
output.write(json.dumps(returnData))