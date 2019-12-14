import requests, json, time, random

header = {"Content-Type": "application/json"}

def post_main(url, header):
    res = requests.post(url=url, headers=header)
    print(res.text)

if __name__ == "__main__":
    while 1:
        post_main("http://127.0.0.1:8000/userInfo/login/", header)
        
    

