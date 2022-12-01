import requests

secure = requests.get("https://httpbin.org/status/200")

print(secure.status_code)

secure.raise_for_status()

secure2 = requests.get("https://httpbin.org/html")

print(secure2.encoding)

print(secure2.text)
print(secure2.content)

#json files
secure3 = requests.get("https://httpbin.org/json")
print(secure3.encoding)
print(secure3.text)
print(secure3.content)