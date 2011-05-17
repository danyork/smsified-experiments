# Really simple python app for playing with sending SMS messages
# via SMSified - http://www.smsified.com/

import json
import urllib

senderid = "danyorksmsified"   #SMSified account
password = "notmyrealpassword" #SMSified password
sendernum = "7177455086"       #SMSified phone number

apiurl = "https://"+senderid+":"+password+"@api.smsified.com/v1/smsmessaging/outbound/"+sendernum+"/requests"

address = "14079678424"        # Phone num to which you want to send msg
message = "Hello there"        # Whatever msg you want to send

data = urllib.urlencode((('address',address),('message',message)))

print apiurl+"?"+data
f = urllib.urlopen(apiurl,data)

print json.loads(f.read())['resourceReference']['resourceURL']

