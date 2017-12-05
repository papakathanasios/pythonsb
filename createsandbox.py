import http.client

conn = http.client.HTTPSConnection("apis.nbg.gr")


#Change the REPLACE_SANDBOX_ID with the id you want for your Sandbox
payload = "{\"sandbox_id\":\"REPLACE_SANDBOX_ID\"}"

headers = {
    'content-type': "text/json",
    'accept': "text/json"
    }

conn.request("POST", "/public/nbgapis/obp/v3.0.1/sandbox", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
