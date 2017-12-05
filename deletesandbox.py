import http.client

conn = http.client.HTTPSConnection("apis.nbg.gr")

#Change REPLACE_SANDBOX_ID with the ID of your sandbox
conn.request("DELETE", "/public/nbgapis/obp/v3.0.1/sandbox/REPLACE_SANDBOX_ID")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
