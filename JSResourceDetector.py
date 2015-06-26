# setup Imports
from burp import IBurpExtender
from burp import IHttpListener
from burp import IHttpRequestResponse
from burp import IResponseInfo
from burp import IExtensionHelpers

# Class BurpExtender (Required) contaning all functions used to interact with Burp Suite API
class BurpExtender(IBurpExtender, IHttpListener):

	# define registerExtenderCallbacks: From IBurpExtender Interface 
	def registerExtenderCallbacks(self, callbacks):
	
		# keep a reference to our callbacks object (Burp Extensibility Feature)
		self._callbacks = callbacks
		# obtain an extension helpers object (Burp Extensibility Feature)
		# http://portswigger.net/burp/extender/api/burp/IExtensionHelpers.html
		self._helpers = callbacks.getHelpers()
		# set our extension name that will display in Extender Tab
		self._callbacks.setExtensionName("JS Resource Detector")
		# register ourselves as an HTTP listener
		callbacks.registerHttpListener(self)
		
	# define processHttpMessage: From IHttpListener Interface 
	def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
		
			# determine if request or response:
			if not messageIsRequest:#only handle responses
				response = messageInfo.getResponse() #get Response from IHttpRequestResponse instance
				analyzedResponse = self._helpers.analyzeResponse(response) # returns IResponseInfo
				url = self._helpers.analyzeRequest(messageInfo).getUrl()
				headerList = analyzedResponse.getHeaders() # get Headers from IResponseInfo Instance
				# iterate though list of headers
				for header in headerList:
					# Look for Content-Type Header)
					# javascript mime type from : http://www.rfc-editor.org/rfc/rfc4329.txt
					if header.startswith("Content-Type:"):
						# Look for javascript/jscript/ecmacscript response
						if ("javascript" in header) or ("jscript" in header) or ("ecmascript" in header):
							 print str(url)