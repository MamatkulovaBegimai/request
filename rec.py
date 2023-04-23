import requests

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"
}

# r = requests.get('https://httpbin.org/get', headers=headers)

# # print(r.status_code)
# # print(r.headers)
# # print(r.content)
# print(r.text)

url = 'https://encrypted-vtbn0.gstatic.com/video?q=tbn:ANd9GcTZznKLNDWis601h0MPVbniatHGe4_1Xn_Wmw'
r = requests.get(url, headers=headers, stream=True)
# print(r.text)
# print(r.content)
# print(r.raw.read(1000))

with open('1.webm', "wb") as fd:
    for chunk in r.iter_content(chunk_size=1024*100):
        fd.write(chunk)
        print("Write chunk 10kb")