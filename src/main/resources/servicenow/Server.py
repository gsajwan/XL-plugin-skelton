#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import sys, string, time
import com.xhaus.jyson.JysonCodec as json
from servicenow.ServiceNowClient import ServiceNowClient

params ={
	'url':configuration.url, 'username':configuration.username 
	, 'password':configuration.password,'useOAuth':configuration.useOAuth
        , 'oauthUsername':configuration.oauthUsername, 'oauthPassword':configuration.oauthPassword 
	, 'clientId':configuration.clientId, 'clientSecret':configuration.clientSecret
	, 'proxyHost': configuration.proxyHost, 'proxyPort':configuration.proxyPort
	, 'changeRecordTableName': configuration.changeRecordTableName
	, 'changeTaskTableName': configuration.changeTaskTableName
	, 'sysparmDisplayValue' : configuration.sysparmDisplayValue
	, 'sysparmInputDisplayValue' : configuration.sysparmInputDisplayValue  
} 

snClient = ServiceNowClient.create_client(params)
content = None

print "Sending content %s" % content

data = snClient.get_scorecards()
