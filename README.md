# 📖 프로젝트명 

### ✔️ 불법 현수막 탐지 프로젝트 (메티버스 아카데미 2기 AI반 8월 월말평가 팀 프로젝트)

# 📃 프로젝트 소개

### ✔️ Yolo(v8), OCR(PaddleOCR,Naver Clovar OCR), ChatGPT를 활용한 불법 현수막 탐지 시스템 프로젝트입니다.

도로변 / 주거단지 근처 거치된 합·불법 현수막을 탐지하고 게시 현황을 시각화하여 제공하는 '불법 현수막 자동 탐지 시스템' 프로젝트입니다.

주제 선정 배경은 크게 3가지입니다.

첫번째로 지자체 (시청/구청) 단속 인력의 부족입니다. 올해  춘천시 기준으로 불법 현수막 단속 작업에 대해 시 전체를 관할하는 인력은 총9명이고, 이 중 6명은 하루 6시간만 근무하는 희망근로자입니다. 직접 이동하여 불법 현수막을 발견하고 철거해야하는 현수막 단속 작업 특성상 많은 시간이 소요되어 보다 많은 인력이 투입되어야하는 상황입니다. 또한 주말에만 몰래 게시하는 일명 '게릴라성 불법 현수막' 형태도 있어 휴일에도 상시인력이 투입되거나 야간 단속작업 횟수를 2배 이상 확대하는 광진구의 사례 또한 발생하고 있습니다. 이러한 이유 때문에 단속 작업을 조금 더 자동화할 필요가 있다고 생각하였습니다.

[춘천시 불법 현수막 단속 작업 인력난](https://www.youtube.com/watch?v=QtI7la0i_7A&ab_channel=%EC%B6%98%EC%B2%9CMBC%EB%89%B4%EC%8A%A4) , 
[광진구 야간 단속 작업 확대](https://www.munhwa.com/news/view.html?no=2022092001031039342001)

두번째로 옥외광고물법 개정안입니다. 작년 12월 개정된 옥외광고물법으로 인해 정치적 목적의 현수막 게시가 합법화되었습니다. 이에 따라 일명 '정당현수막'이 우후죽순으로 늘어났습니다. 관련 민원 현황으로

![image](https://github.com/MTVS-AI/META_Yolo_OCR_ChatGPT_PJT/assets/115389344/4f5bdb40-8165-4a6d-91b3-c14c1907fdc3)

[정당현수막 민원 현황](http://ccej.or.kr/location_post/%EB%85%BC%ED%8F%89-%E8%88%87%E9%87%8E%E2%80%A7%EC%A0%95%EB%B6%80-%EC%A3%BC%EB%AF%BC-%EC%95%88%EC%A0%84%EA%B6%8C-%EB%93%B1-%EC%9C%84%ED%95%B4-%EB%A7%88%EB%A0%A8%ED%95%B4%EC%95%BC)

지방자치단체에 접수된 민원의 숫자가 2배에서 심한 곳은 5배 넘게 증가한 곳도 존재했습니다. 이는 게시 기간만 명시한다면 개수/장소의 제한없이 설치할 수 있는 현행법 상의 이유입니다. 최근 국회에서도 이에 대한 문제점을 인식하여 개수/장소를 제한하는 법안을 발행중이며 해당 법안이 통과되었을 시 이번 프로젝트를 활용하여 시간/구역별로 게시 현황을 파악할 수 있을 것입니다. 

세번째로 보행자 사고 예방 목적입니다. 최근 언론에서 자전거 전용도로를 달리던 자전거를 향해 바람에 휘발린 불법 현수막이 덮침으로 인해 발생한 전치 3주 이상의 상해 사례, 현수막 줄에 걸린 가로등이 강풍에 뽑혀 도로를 건너던 행인의 머리를 가격하는 사례들이 발생하고 있음을 보도했습니다. 불법 길거리 현수막으로 인한 사고는 큰 인명 피해를 야기하기에 이를 사전에 탐지하여 예방하는 목적으로 개발하였습니다.<br><br>
[불법현수막 사고 사례(1)](https://www.tbc.co.kr/news/view?c1=8news&c2=&pno=20230419135908AE08505&id=177714) , 
[불법현수막 사고 사례(2)](https://news.imaeil.com/page/view/2023030210490378827)

기술적인 프로세스로써 사전에 수집한 차량 운행 데이터를 Object Detection(Yolov8)을 활용하여 합/불법 현수막을 추출하고 OCR(PaddleOCR, Naver Clova OCR)을 활용하여 각 현수막별 텍스트를 추출한뒤 ChatGPT API를 활용하여 현수막별 대분류, 합/불법 유무를 파악하는 과정을 구현하였습니다.

# 👩‍🔧 팀원 소개 및 역할

### ✔️ 팀원
메타버스 아카데미 2기 AI반 김종민, 나인채, 차민수, 임정민 총 4명

### ✔️ 역할 분담

주제 선정 : 모든 팀원 토의 및 강사/멘토님 협조

시청/구청 관계자 인터뷰 : 차민수

데이터 서치/수집 : 모든 팀원<br><br>
🔹총 1342개 현수막 이미지 데이터<br>
🔹도로변/인도 주변 현수막 실촬영, 인원별 100장 (약 400장)<br>
🔹Bing 이미지 검색 크롤링 약 50장 <br>
🔹네이버,카카오맵 로드뷰 캡처 약 900장 <br>

데이터 전처리 : 모든 팀원<br><br>
🔹Roboflow 활용 전체 데이터셋의 1/n씩 Boxes Annotation <br>

모듈 개발 역할<br><br>
🔹Yolo(v8) 모델 학습 및 평가 : 김종민, 임정민<br> 
🔹OCR(PaddleOCR, Naver Clova OCR) 모듈 개발 : 차민수<br>
🔹ChatGPT 프롬프트 엔지니어링 : 나인채, 임정민<br>
🔹Flask 서빙 서버 개발 : 김종민, 나인채<br>
🔹React UI 서버 개발 : 나인채<br>
🔹Folium 지도 모듈 개발 : 차민수<br>

개발 코드 통합 : 임정민<br><br>
통합 코드 모듈회 : 나인채, 김종민

발표 PPT 및 대본 : 임정민

PT 발표 : 알파 - 차민수, 베타 - 김종민, 최종 - 나인채

# 📅프로젝트 진행 기록

### ✔️ 수행 기간
2023.08.01 ~ 2023.08.29

### ✔️ 세부 진행 기록
- 23-08-01 : 팀 아이스브레이킹(선호 기술 토의),주제 토의(1)
- 23-08-02 : 아이디어 피드백, 주제 토의(2), 데이터 서치(AI hub, 공공데이터포털)
- 23-08-03 : 아이디어 심사, 주제 선정, 데이터 서치(AI hub, 공공데이터포털), 활용 기술 파악(Obejct Detection, OCR, Text Classification)
- 23-08-04 : 도로변/인도 주변 현수막 실촬영 데이터 수집(야간), Yolov8 객체 탐지 모델 검토
- 23-08-05 ~ 23-08-06 : 도로변/인도 주변 현수막 실촬영 데이터 수집(주간/야간)
- 23-08-07 : 팀별 프로젝트 주제 발표
- 23-08-08 : Roboflow 활용 1차 Annotation, yolov8n.pt Pretrained 모델 학습
- 23-08-09 : yolov8n.pt Fine-tunning 모델 평가, 추가 데이터 수집 계획 수립(크롤링 및 로드뷰 활용)
- 23-08-10 : 네이버/카카오맵 로드뷰 활용 현수막 이미지 수집(1), Roboflow 활용 2차 Annotation(1)
- 23-08-11 : 네이버/카카오맵 로드뷰 활용 현수막 이미지 수집(2), Roboflow 활용 2차 Annotation(2), 총 1342개 현수막 이미지 데이터셋 구성
- 23-08-12 ~ 23-08-13 : yolov8n.pt 기반 Fine-tunning 진행,  yolov8s.pt 기반 Fine-tunning 진행
- 23-08-14 : 진행상황 중간보고, 가상환경 통합, Yolo/OCR/chatGPT Main코드 통합 작업(1)
- 23-08-15 : 휴식 (광복절)
- 23-08-16 : Yolo/OCR/chatGPT Main코드 통합 작업(2),flask작업시작, yolo8_s 학습진행, Naver CLOVA OCR API 코드 구현
- 23-08-17 : yolo8_s(epochs=108)영상시연, flask 파일 및 폴더 업로드구현, Clova OCR & chatGPT API 코드 통합
- 23-08-18 : yolov8s.pt/yolov8m.pt 기반 Fine-tunning 진행, Folium 기반 지도 모듈 구현, flask 불필요한 파일 업로드 제외처리구현
- 23-08-19 ~ 23-08-20  : Folium 기반 지도 모듈 구현, 프로젝트 베타버전 PPT/대본 작성, YOLO&OCR&GPT 함수화 작업 및 py변환, FrontEnd(BootStrap), Naver Map api 구축
- 23-08-21 : 팀별 프로젝트 베타버전 발표, 베타버전 피드백 및 회의
- 23-08-22 : 전체 모듈 속도 테스트, Folium 기반 시각화 속도 개선  
- 23-08-23 : 이미지 선명화 및 기존 이미지와 비교작업 진행
- 23-08-24 : yolov8(n) 파라미터 튜닝(dropout=0.3 레이어 추가), 서비스 서버/모델 서버 호환 작업(1)
- 23-08-25 : 서비스 서버/모델 서버 호환 작업(2)
- 23-08-26 ~ 23-08-27  : 실전 데이터 수집 (총 10개 현수막 데이터), 실전 데이터 구동, 최종 UI 및 UX개선
- 23-08-28 : PPT/대본 작성, 블로그/깃허브 정리, 발표 리허설
- 23-08-29 : 최종 PT 발표 및 질의응답, 팀 회식 

# 📊 데이터 소개
### ✔️ 도로변/인도 주변 현수막 실촬영 데이터 400장 (개별 100장)
              
![image](https://github.com/MTVS-AI/META_Yolo_OCR_ChatGPT_PJT/assets/115389344/d0bbbfe0-cb26-4c71-a19f-ac315ea85779)

### ✔️ 네이버 지도/카카오맵 로드뷰 캡쳐 (약 900장)

![image](https://github.com/MTVS-AI/META_Yolo_OCR_ChatGPT_PJT/assets/115389344/26235036-8a9c-4fb9-bbdb-dd729c074c6e)

### ✔️ Bing 이미지 검색 크롤링 (약 50장)

![image](https://github.com/MTVS-AI/META_Yolo_OCR_ChatGPT_PJT/assets/115389344/be2e84d9-3e73-4db3-89fd-84b7a072b0f3)

### ✔️ 데이터 세부 사항

- 원본 데이터 갯수 : 1342개<br>
- 데이터 증강 방법 (차량 주행 시점 고려)
  1) rotate ± 10°
  2) brightness ± 25%
  3) saturation ± 25%
- 총 학습 데이터 갯수 : 3226개 (train:2826개, valid:268개, test:132개)
- 클래스 : banner(현수막), frame(지정게시대틀) 총 2개 클래스

# 💡 주요 내용

### ✔️ Object Detection

##### yolov8(n)

### ✔️ OCR
##### 1) PaddleOCR

- 경계가 뚜렷한 텍스트와 숫자 추출에 괜찮은 성능을 보였다.
- 희미한 텍스트에 대해 색상 반전 등의 기법을 시도했다.
- 그러나 다음단계로 넘어갔을 때 PaddleOCR로 추출한 텍스트만으로는 현수막 분류가 불가능하여 다른 OCR을 활용했다.


##### 2) Naver Clova OCR

- Naver Clova에서 API를 발급받아 요금을 내고 사용하는 고성능 OCR 모듈
- PaddleOCR보다 기울어진 구도의 현수막과, Noise가 들어가있는 텍스트들을 더 효과적으로 추출 가능했다.


### ✔️ 텍스트 분류 (ChatGPT)

- OCR을 통해 추출된 현수막의 텍스트 카테고리 분류 (프레임/합법/정치/기타 총 4개 클래스)
- chatGPT API활용 Text Classification

### 🗺️ 웹서비스 기반 지도 시각화

##### ✔️ 들어가는 정보
- 정제된 DataFrame 바탕
- 이미지 / 이미지의 종류
- 내용 : crop된 이미지의 범례, 현수막의 내용, 해당 범례로 분류한 근거를 표의 형태로 포함

##### ✔️ folium 모듈
- leaflet.js를 기반으로 만들어진 Python 지도 시각화 라이브러리
- 좌표값을 기반으로 popup 마커를 생성하며, 해당 마커들은 범례에 따라 하나의 그룹으로 묶는다.
- popup에는 html 기반의 표가 들어가며, base64를 통해 인코딩 및 디코딩해서 이미지를 표에 삽입한다.
- 지도에는 최종적으로 popup 마커들이 표시되며, 우측 상단의 박스 체크를 통해 합법 / 정치 / 불법 현수막들 중 원하는 종류의 현수막 현황을 볼 수 있게 조절 가능하다.

# 🛠 기술 스택

### 🔹 언어
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=python&logoColor=white">

### 🔹 주요 라이브러리
<img src="https://img.shields.io/badge/tensorflow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"> <img src="https://img.shields.io/badge/pytorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"> <img src="https://img.shields.io/badge/torchvision-29A7DF?style=for-the-badge&logo=torchvision&logoColor=white"> <img src="https://img.shields.io/badge/opencv-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"> <img src="https://img.shields.io/badge/MediaPipe-1299F3?style=for-the-badge&logo=MediaPipe&logoColor=white"> <img src="https://img.shields.io/badge/facenetpytorch-FF5500?style=for-the-badge&logo=facenetpytorch&logoColor=white"> <img src="https://img.shields.io/badge/keras-D00000?style=for-the-badge&logo=keras&logoColor=white"> <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"> <img src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white"> <img src="https://img.shields.io/badge/matplotlib-0058CC?style=for-the-badge&logo=matplotlib&logoColor=white"> <img src="https://img.shields.io/badge/pillow-006AFF?style=for-the-badge&logo=pillow&logoColor=white">

### 🔹 개발 툴
<img src="https://img.shields.io/badge/VS code-2F80ED?style=for-the-badge&logo=VS code&logoColor=white"> <img src="https://img.shields.io/badge/Google Colab-F9AB00?style=for-the-badge&logo=Google Colab&logoColor=white">

### 🔹 협업 툴
<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"> <img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white">

# 🔍 참고 자료

### ✔️ 기사

- https://www.youtube.com/watch?v=QtI7la0i_7A&ab_channel=%EC%B6%98%EC%B2%9CMBC%EB%89%B4%EC%8A%A4
- https://www.munhwa.com/news/view.html?no=2022092001031039342001
- https://www.joongang.co.kr/article/25170006#home
- https://www.busan.com/view/busan/view.php?code=2023061418340018356
- https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0002429221
- https://www.greenkorea.org/activity/living-environment/zerowaste/91981/

### ✔️ 오픈소스 (GitHub)

- https://github.com/ultralytics/ultralytics
- https://www.ncloud.com/product/aiService/ocr

### ✔️ 라이브러리 공식 문서

- https://docs.ultralytics.com/modes/predict/
- https://pypi.org/project/paddleocr/
