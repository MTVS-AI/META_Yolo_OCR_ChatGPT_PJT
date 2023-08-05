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



for address in addresses:
    # Google Maps Geocoding API로 주소를 위도, 경도로 변환
    geocoding_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key=YOUR_GEOCODING_API_KEY"
    geocoding_response = requests.get(geocoding_url)
    geocode = geocoding_response.json()

    lat = geocode['results'][0]['geometry']['location']['lat']
    lng = geocode['results'][0]['geometry']['location']['lng']

    # Google Street View API를 통해 로드뷰 이미지를 가져옴
    street_view_url = f"https://maps.googleapis.com/maps/api/streetview?size=600x300&location={lat},{lng}&fov=80&heading=70&pitch=0&key=YOUR_STREET_VIEW_API_KEY"
    image_response = requests.get(street_view_url)

    # 로드뷰 이미지를 파일로 저장
    with open(f'roadview_{address}.jpg', 'wb') as f:
        f.write(image_response.content)

    # 이미지를 화면에 출력
    img = mpimg.imread(f'roadview_{address}.jpg')
    imgplot = plt.imshow(img)
    plt.show()