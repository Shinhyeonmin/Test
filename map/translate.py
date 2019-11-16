import os
import sys
import urllib.request
import json
client_id = "XhFUNhV0yVzNSlqiFpQ4"
client_secret = "44VHftFxNI"

while(True):
    word = int(input('번역할 언어(영어, 한국어'))
    if(word == 1):
        word = 'en'
    elif(word == 2):
        word = 'ko'

    num = int(input('1.미 2.한국어 3.중_간 4.중_번 5.스페인 6.프 7.베트남 8.태국 9.인도네시아 10.일본'))
    if(num ==1):
        num = 'en'
    elif(num == 2):
        num = 'ko'
    elif(num == 3):
        num = 'zh-CN'
    elif(num == 4):
        num = 'zh-TW'
    elif(num == 5):
        num = 'es'
    elif(num == 6):
        num = 'fr'
    elif(num == 7):
        num = 'vi'
    elif(num == 8):
        num = 'th'
    elif(num == 9):
        num = 'id'
    elif(num == 10):
        num = 'ja'

    if(word == num):
        print('둘중 하나를 다시 선택하세요')
    else:
        break

#여기서 입력 할거 만들기

with open('source.txt', 'r', encoding='utf8') as f:
    srcText = f.read()

encText = urllib.parse.quote(srcText)
data = "source="+word+"&target="+num+"&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
a = input('w와 a만 들어 갈 수 있습니다.(w는 써있는 거 다 삭제, a는 기존 거 옆에 번역)')
if(rescode == 200):
    response_body = response.read()

    res = json.loads(response_body.decode('utf-8'))

    with open('translate.txt', a, encoding='utf-8') as f:
        f.write(res['message']['result']['translatedText'])

else:
    print("Error Code:" + rescode)