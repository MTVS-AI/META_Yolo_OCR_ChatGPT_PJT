from PIL import Image
import pytesseract
import re
import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 이미지 로드
img = Image.open('image.jpg')
# OCR 적용
text = pytesseract.image_to_string(img, lang='eng')
print(text)
# 숫자와 문자가 섞인 간단한 주소를 찾는 정규표현식
regex = r'\d+ [\w\s]+'
addresses = re.findall(regex, text)
print(addresses)

HEADERS = {
    "X-NCP-APIGW-API-KEY-ID": "YOUR_NAVER_CLIENT_ID",
    "X-NCP-APIGW-API-KEY": "YOUR_NAVER_CLIENT_SECRET"
}

for address in addresses:
    # 네이버 Geocoding API로 주소를 위도, 경도로 변환
    geocoding_url = f"https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={address}"
    geocoding_response = requests.get(geocoding_url, headers=HEADERS)
    geocode = geocoding_response.json()
    
    lat = geocode['addresses'][0]['y']
    lng = geocode['addresses'][0]['x']

    # 네이버 로드뷰 이미지 API
    street_view_url = f"https://naveropenapi.apigw.ntruss.com/map-streetview/v2/view?coord={lng},{lat}&w=600&h=300&format=jpg"
    image_response = requests.get(street_view_url, headers=HEADERS)
    
    # 로드뷰 이미지를 파일로 저장
    filename = f'roadview_{address}.jpg'
    with open(filename, 'wb') as f:
        f.write(image_response.content)

    # 이미지를 화면에 출력
    img = mpimg.imread(filename)
    imgplot = plt.imshow(img)
    plt.show()