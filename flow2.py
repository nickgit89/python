import requests


get2 = requests.get("http://httpbin.org/xml")

print(get2.status_code)
print(get2.text)

arg = {"key1" : "tomorrow", "key2": False, "key3": 22}

get2 = requests.get("http://httpbin.org/get", params = arg)

print(get2.text)
print(get2.url)


#posting

get2 = requests.post("http://httpbin.org/post", data = {"klaus": "december 25"})
print(get2.text)