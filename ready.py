import requests

status = requests.get('https://api.github.com/events')


if status == "<Response [200]>":
    print("you were able to reach the website")

postthis = requests.post('https://httpbin.org/post', data={'Vacation': 'the best'})

#https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request