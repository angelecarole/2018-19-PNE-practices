import http.client
import json

HOSTNAME = "www.metaweather.com"
ENDPOINT_SEARCH_WOEID = "/api/location/search/"
ENDPOINT = "/api/location/"
METHOD = "GET"

info = input("insert a city please: ")

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT_SEARCH_WOEID + '?query=' + info, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

city = json.loads(text_json)
list = city[0]
woeid = list['woeid']

print('The woeid is: {}'.format(woeid))

conn.request(METHOD, ENDPOINT + str(woeid) + '/', None, headers)
