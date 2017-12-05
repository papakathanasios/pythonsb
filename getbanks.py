import http.client

conn = http.client.HTTPSConnection("apis.nbg.gr")

#Replace the header values with the values you got when you created your sandbox
headers = {
    'accept': "text/json",
    'sandbox_id': "REPLACE_THIS_VALUE",
    'application_id': "REPLACE_THIS_VALUE",
    'user_id': "REPLACE_THIS_VALUE",
    'username': "REPLACE_THIS_VALUE",
    'provider_id': "REPLACE_THIS_VALUE",
    'provider': "REPLACE_THIS_VALUE"
    }

conn.request("GET", "/public/nbgapis/obp/v3.0.1/banks", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
