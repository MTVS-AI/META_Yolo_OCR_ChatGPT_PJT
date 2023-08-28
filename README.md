# 📖 프로젝트명

### ✔️ 불법 현수막 탐지 프로젝트 (메티버스 아카데미 2기 AI반 8월 월말평가 팀 프로젝트)

# 📃 프로젝트 소개

### ✔️ Yolo(v8), OCR(PaddleOCR,Naver Clovar OCR), ChatGPT를 활용한 불법 현수막 탐지 시스템 프로젝트입니다.

도로변 / 주거단지 근처 거치된 합·불법 현수막을 탐지하고 게시 현황을 시각화하여 제공하는 '불법 현수막 자동 탐지 시스템' 프로젝트입니다.

주제 선정 배경은 크게 3가지입니다.

첫번째로 지자체 (시청/구청) 단속 인력의 부족입니다. 올해  춘천시 기준으로 불법 현수막 단속 작업에 대해 시 전체를 관할하는 인력은 총9명이고, 이 중 6명은 하루 6시간만 근무하는 희망근로자인 상황인데 직접 이동하여 불법 현수막을 발견하고 철거해야하는 현수막 단속 작업 특성상 많은 시간이 소요되어 보다 많은 인력이 투입되어야하는 상황입니다. 또한 주말에만 몰래 게시하는 게릴라성 불법 현수막 때문에 휴일에도 상시인력이 투입되거나 야간 단속작업 횟수를 2배 이상 확대하는 광진구의 사례도 있기 때문에 이러한 단속 작업을 조금 더 자동화할 필요가 있다고 생각하였습니다.

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
🔹ChatGPT 프롬프트 엔지니어링 : 나인채<br>
🔹Flask 서빙 서버 개발 : 김종민<br>
🔹React UI 서버 개발 : 나인채<br>
🔹Folium 지도 모듈 개발 : 차민수<br>

개발 코드 통합 : 임정민

발표 PPT 및 대본 작성 : 모든 팀원  

PT 발표 : 차민수

# 📅프로젝트 진행 기록

### ✔️ 수행 기간
2023.08.01 ~ 2023.08.31

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
- 23-08-26 ~ 23-08-27  : 실전 데이터 수집 (총 10개 현수막 데이터), 실전 데이터 구동
- 23-08-28 : PPT/대본 작성, 블로그/깃허브 정리
- 23-08-29 : 최종 PT 발표 및 질의응답, 팀 회식 

- 23-07-18 (9:00 ~ 14:00) : cv2 활용 카메라(웹캠) 테스트, 각도별 안면 데이터 수집
- 23-07-18 (14:00 ~ 20:00) : DataFrame 활용 Multi-Label 형식 전처리 
- 23-07-19 : 안면 인식을 위한 MediaPipe, FaceNet(MTCNN)모듈 성능 테스트, 카메라(웹캠) 연동 모듈 개발
- 23-07-20 : 팀원별 할당된 CNN 아키텍처 Transfer Learning Multi-Label 분류 학습, 카메라/Face-Recognition/CNN 분류 통합 모듈 개발
- 23-07-21 (9:00 ~ 12:00): CNN 모델 튜닝 및 재학습, PPT 초안 및 대본 작성
- 23-07-21 (13:00 ~ 22:00): PPT/대본 작성, 블로그/깃허브 정리

  ++
- 23-07-31 : AI 전공 내부 발표 및 질의응답

# 📊 데이터 소개
### ✔️ 도로변/인도 주변 현수막 실촬영 데이터 400장 (개별 100장)

　　　　　　　　　　　　　<주간>　　　　　　　　　　　　　　　　　　　　　　　　　　　　　<야간>
              
![image](https://github.com/MTVS-AI/META_Yolo_OCR_ChatGPT_PJT/assets/115389344/d0bbbfe0-cb26-4c71-a19f-ac315ea85779)

### ✔️ 네이버 지도/카카오맵 로드뷰 캡쳐 (약 900장)

![image](https://github.com/MTVS-AI/META_Yolo_OCR_ChatGPT_PJT/assets/115389344/26235036-8a9c-4fb9-bbdb-dd729c074c6e)

### ✔️ Bing 이미지 검색 크롤링 (약 50장)

![image](https://github.com/MTVS-AI/META_Yolo_OCR_ChatGPT_PJT/assets/115389344/be2e84d9-3e73-4db3-89fd-84b7a072b0f3)

### ✔️ 데이터 세부 사항

- 총 데이터 갯수 : 1342개<br>
- 남녀 비율 각 45%, 55%
- 3014명의 이미지 데이터
- 10대 연령이 27%로 가장 많은 비율 차지
- 40대 연령이 24%로 두번째로 많은 비율 차지
- 여러 각도의 이미지 데이터
- 다양한 밝기/환경의 이미지 데이터


# 💡 주요 내용

### ✔️ 카메라(웹캠) 모듈

1. Opencv 활용 노트북 웹캠 연동
2. 짧은 대중교통 / 엘리베이터 탑승 시간을 고려하여 실시간 영상에서 10초에 한번씩 Capture하게 설정
3. 영상에서 캡쳐된 frame을 BGR2RGB Color 변환하여 Face-Recognition 모델로 전달

### ✔️ Face-Recognition

1. 안면 검출을 위한 모듈(MediaPipe, FaceNet(MTCNN)) 서치
2. 1920x1080 이미지 데이터 1000개 기준 Inference 속도 비교
3. 짧은 시간 탑승하는 대중교통/엘리베이터 특성 고려 =>  추론 속도 기준 약 3배 빠른 MediaPipe를 프로젝트에 활용

![image](https://github.com/haeniKim/ai-project-team4/assets/115389344/c051b558-d4db-4e09-b34a-f9e789c18d4d)

4. MediaPipe를 활용한 안면 이미지 Crop 시, 이목구비까지만 추출되어 저조한 성별 분류 정확도를 보였음  => 추출되는 안면 이미지 frame을 확장하여 얼굴형/헤어 스타일까지 포함되게끔 Crop

### ✔️ CNN Multi-Label 데이터 전처리 

1. 다양한 각도/연령별 안면 데이터가 포함된 'AI-Hub '가족 관계가 알려진 얼굴 이미지 데이터' 활용
2. 해당 데이터 중 전문 스튜디오에서 촬영된 정제된 데이터 제외, 야외에서 촬영된 데이터만 활용
3. Multi-Label을 위한 이미지 데이터별 성별/연령 Labeling (Dataframe 활용)

![image](https://github.com/haeniKim/ai-project-team4/assets/115389344/73b4fe21-2222-4c6b-8cc7-7f5a1973a585)

[Multi-Label 참고 링크](https://vijayabhaskar96.medium.com/multi-label-image-classification-tutorial-with-keras-imagedatagenerator-cd541f8eaf24)

### ✔️ CNN Multi-Label 모델 학습 및 Evaluate Accuaracy

1. EfficientNetB0 (weights='imagenet', epochs=10(Early Stopping), optim=Adam, lr=0.001,batch_size=16)<br>
   🔹Accuracy = 0.5628
   🔸Loss = 0.5628
3. VGG16 (weights='imagenet', epochs=10(Early Stopping), optim=Adam, lr=0.001,batch_size=16)<br>
   🔹Accuracy = 0.8087
   🔸Loss = 2.5519
5. DenseNet121Net (weights='imagenet', epochs=10(Early Stopping), optim=Adam, lr=0.001,batch_size=16)<br>
   🔹Accuracy = 0.9432
   🔸Loss = 0.1323
7. ResNet50 (weights='imagenet', epochs=10(Early Stopping), optim=Adam, lr=0.001,batch_size=16)<br>
   🔹Accuracy = 0.8702
   🔸Loss = 0.3131

### ✔️ 성별/연령 분류에 따른 광고 송출

![image](https://github.com/haeniKim/ai-project-team4/assets/115389344/ffa46364-dbac-461b-a341-fb54422ca627)

   
### ✔️ 결과

- 최적의 Accuracy, Loss 지표를 보이는 DenseNet121 모델 선정<br><br>
DenseNet121Net (weights='imagenet', epochs=15(Early Stopping), optim=Adam, lr=0.00001,batch_size=16)<br>
🔹Accuracy = 0.9513 🔸Loss = 0.1346 <br><br>
![image](https://github.com/haeniKim/ai-project-team4/assets/115389344/7f7636b7-2d14-4d91-b7e0-0f482ae61a36)

- 기대 효과
1) 광고주 : 타겟층이 인식될 때만 광고를 송출하기 때문에 광고료 효율성이 증가할 것으로 예상됩니다.<br>
2) 소비자 : 연령과 성별에 맞는 광고 송출로 관심 있는 제품에 집중 가능하며, 불필요한 정보 혼란을 줄일 수 있어 효율적인 쇼핑이 가능할 것입니다.<br>
3) 지역 커뮤니티 연계: 지하철, 버스 정류장 등의 지역과 시간대 별 인구특성 파악을 통해 새로운 마케팅 전략 수립과 지역 사회와의 협력을 통한 개인화된 서비스 제공이 가능해질 것으로 보입니다.<br>

- 한계점 및 개선방안
1) 분류 정확도 최적화: 연령별 클래스를 축소한다면 (ex: 10대와 20대 통합, 30대와 40대 통합) 정확도를 상승을 도모할 수 있을 것입니다.<br>
2) 데이터 불균형: 연령별 데이터 불균형은 서비스 이용자 데이터를 수집하여 모델에 반영할 계획입니다.<br>
3) 추론 시간 단축: 가중치 압축을 통해 이미지 인식과 추론 시간을 단축시킬 예정입니다.<br>
4) 추천 알고리즘 활용: 성별/연령 기반 광고 송출 대신 타겟 별 추천 알고리즘을 사용하여 광고를 송출할 계획입니다.<br>
5) 시선 추적 기술: 미래에 기술이 가능해진다면, 많은 사람이 탐지될 때 광고 타겟층을 명확히 하기 위해 시선 추적 기술을 사용하여 광고판을 바라보는 사람만 타겟으로 인식해 광고를 송출할 예정입니다.<br>

# 🛠 기술 스택

### 🔹 언어
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">

### 🔹 주요 라이브러리
<img src="https://img.shields.io/badge/tensorflow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"> <img src="https://img.shields.io/badge/pytorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"> <img src="https://img.shields.io/badge/torchvision-29A7DF?style=for-the-badge&logo=torchvision&logoColor=white"> <img src="https://img.shields.io/badge/opencv-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"> <img src="https://img.shields.io/badge/MediaPipe-1299F3?style=for-the-badge&logo=MediaPipe&logoColor=white"> <img src="https://img.shields.io/badge/facenetpytorch-FF5500?style=for-the-badge&logo=facenetpytorch&logoColor=white"> <img src="https://img.shields.io/badge/keras-D00000?style=for-the-badge&logo=keras&logoColor=white"> <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"> <img src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white"> <img src="https://img.shields.io/badge/matplotlib-0058CC?style=for-the-badge&logo=matplotlib&logoColor=white"> <img src="https://img.shields.io/badge/pillow-006AFF?style=for-the-badge&logo=pillow&logoColor=white">

### 🔹 개발 툴
<img src="https://img.shields.io/badge/VS code-2F80ED?style=for-the-badge&logo=VS code&logoColor=white"> <img src="https://img.shields.io/badge/Google Colab-F9AB00?style=for-the-badge&logo=Google Colab&logoColor=white">

### 🔹 협업 툴
<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"> <img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white">

# 🔍 참고 자료
### ✔️ 데이터
  
![image](https://github.com/haeniKim/ai-project-team4/assets/115389344/842f0c23-673e-462a-8d23-fbe806201144)

[가족 관계가 알려진 얼굴 이미지 데이터](https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=528) <br><br>

### ✔️ 논문

- EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks
- Deep Residual Learning for Image Recognition
- Very Deep Convolutional Networks for Large-Scale Image Recognition
- Densely Connected Convolutional Networks

### ✔️ 기사

- http://www.banronbodo.com/news/articleView.html?idxno=21340
- https://www.etnews.com/20221115000257
- https://www.brandbrief.co.kr/news/articleView.html?idxno=5995
- https://www.jeonmae.co.kr/news/articleView.html?idxno=942925
- http://www.banronbodo.com/news/articleView.html?idxno=21340

### ✔️ 이미지 영상 출처

- https://dimg.donga.com/wps/NEWS/IMAGE/2020/01/03/99072357.2.jpg
- https://url.kr/q6u1no
- https://www.youtube.com/watch?v=EFkdgVDP3qs
